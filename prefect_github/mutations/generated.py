"""
This is a module containing:
GitHub mutation tasks

"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials
from prefect_github.graphql.generated import _subset_return_fields, execute_graphql
from prefect_github.schemas import graphql_schema
from prefect_github.utils import initialize_return_fields_defaults, strip_kwargs

config_dir = Path(__file__).parent.resolve() / ".." / "configs" / "mutation"
return_fields_defaults = {}
for config_path in config_dir.glob("*.json"):
    return_fields_defaults.update(initialize_return_fields_defaults(config_path))


@task(name="add_pull_request_review.add_pull_request_review")
async def add_pull_request_review(  # noqa
    pull_request_id: str,
    github_credentials: GitHubCredentials,
    commit_oid: datetime = None,
    body: str = None,
    event: graphql_schema.PullRequestReviewEvent = None,
    comments: Iterable[graphql_schema.DraftPullRequestReviewComment] = None,
    threads: Iterable[graphql_schema.DraftPullRequestReviewThread] = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Adds a review to a Pull Request.

    Args:
        pull_request_id: The Node ID of the pull request to modify.
        github_credentials: Credentials to use for authentication with GitHub.
        commit_oid: The commit OID the review pertains to.
        body: The contents of the review body comment.
        event: The event to perform on the pull request review.
        comments: The review line comments.
        threads: The review line comment threads.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/mutation/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    op_selection = op.add_pull_request_review(
        **strip_kwargs(
            input=dict(
                pull_request_id=pull_request_id,
                commit_oid=commit_oid,
                body=body,
                event=event,
                comments=comments,
                threads=threads,
            )
        )
    ).pull_request_review(**strip_kwargs())

    op_stack = (
        "addPullRequestReview",
        "pullRequestReview",
    )
    op_selection = _subset_return_fields(
        op_selection, op_stack, return_fields, return_fields_defaults
    )

    result = await execute_graphql.fn(op, github_credentials)
    return result["addPullRequestReview"]["pullRequestReview"]
