from pathlib import Path
from typing import Any, Dict

from prefect import flow, get_run_logger, task

from prefect_github import GitHubCredentials
from prefect_github.mutations import add_comment_subject, add_pull_request_review
from prefect_github.repository import (
    query_repository_pull_request,
    query_repository_pull_requests,
)

# from prefect.deployments import DeploymentSpec
# from prefect.flow_runners import SubprocessFlowRunner


PREFECT_COLLECTIONS = [
    "prefect-airbyte",
    "prefect-aws",
    "prefect-azure",
    "prefect-email",
    "prefect-gcp",
    "prefect-github",
    "prefect-great-expectations",
    "prefect-openmetadata",
    "prefect-shell",
    "prefect-slack",
    "prefect-dask",
    "prefect-ray",
    "prefect-snowflake",
    "prefect-sqlalchemy",
    "prefect-twitter",
]


@task
def get_github_credentials():
    token_path = Path("~/.secrets/github").expanduser()
    with open(token_path, "r") as f:
        token = f.read().strip()
    github_credentials = GitHubCredentials(token=token)
    return github_credentials


@flow
def merge_dependabot_pull_request(
    repository_name: str, pull_request_title: str, repository_owner: str = "PrefectHQ"
) -> Dict[str, Any]:
    logger = get_run_logger()
    logger.info(f"Locating {pull_request_title} PR for {repository_name}...")

    github_credentials = get_github_credentials()

    # subset pull requests by labels
    repository_kwargs = dict(
        owner=repository_owner,
        name=repository_name,
        github_credentials=github_credentials,
    )
    number_nodes = query_repository_pull_requests(
        states=["OPEN"],
        labels=["github_actions", "dependencies"],
        return_fields=["number"],
        first=5,
        **repository_kwargs,
    ).result()["nodes"]

    # find the pull request that matches the provided title
    for number_node in number_nodes:
        pull_request = query_repository_pull_request(
            number=number_node["number"], **repository_kwargs
        ).result()
        if pull_request["title"] == pull_request_title:
            pull_request_id = pull_request["id"]
            break
    else:
        raise ValueError(f"No pull requests found that match: " f"{pull_request_title}")

    # automatically approve the pull request
    pull_request_review = add_pull_request_review(
        pull_request_id=pull_request_id,
        github_credentials=github_credentials,
        event="APPROVE",
        body="Approval done through a prefect-github flow!",
        return_fields=["id"],
    )

    # this will merge the PR if all checks pass
    add_comment_subject(
        subject_id=pull_request_id,
        body="@dependabot merge",
        github_credentials=github_credentials,
        wait_for=[pull_request_review],
    )
    return pull_request


if __name__ == "__main__":
    for repository_name in PREFECT_COLLECTIONS:
        param_flow_name = f"{merge_dependabot_pull_request}_{repository_name}"
        pull_request = merge_dependabot_pull_request.with_options(name=param_flow_name)(
            repository_name=repository_name,
            repository_owner="PrefectHQ",
            pull_request_title="__ENTER_SOMETHING_HERE__",
        )

# DeploymentSpec(
#     flow=merge_dependabot_pull_request,
#     tags=["github", "dependabot"],
#     flow_runner=SubprocessFlowRunner(),
#     parameters={
#         "repository_name": "prefect-twitter",
#         "pull_request_title": "__ENTER_SOMETHING__",
#         "repository_owner": "PrefectHQ"
#     }
# )
