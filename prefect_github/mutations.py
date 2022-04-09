"""This is a module for interacting with GitHub create_pull_request tasks"""


from pathlib import Path

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials
from prefect_github.schemas import graphql_schema


@task
def create_pull_request(
    repository_id: str,
    base_ref_name: str,
    head_ref_name: str,
    title: str,
    github_credentials: GitHubCredentials,
    body: str = None,
    maintainer_can_modify: bool = None,
    draft: bool = None,
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Mutation)
    op_settings = op.create_pull_request(
        input=dict(
            repository_id=repository_id,
            base_ref_name=base_ref_name,
            head_ref_name=head_ref_name,
            title=title,
            body=body,
            maintainer_can_modify=maintainer_can_modify,
            draft=draft,
        )
    )

    result = endpoint(op)
    return result["data"]["createPullRequest"]["pullRequest"]


@task
def create_issue(
    repository_id: str,
    title: str,
    assignee_ids: str,
    label_ids: str,
    project_ids: str,
    github_credentials: GitHubCredentials,
    body: str = None,
    milestone_id: str = None,
    issue_template: str = None,
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Mutation)
    op_settings = op.create_issue(
        input=dict(
            repository_id=repository_id,
            title=title,
            body=body,
            assignee_ids=assignee_ids,
            milestone_id=milestone_id,
            label_ids=label_ids,
            project_ids=project_ids,
            issue_template=issue_template,
        )
    )

    result = endpoint(op)
    return result["data"]["createIssue"]["issue"]
