"""
This is a module for interacting with GitHub Mutation tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from typing import Any, Dict

from prefect import task
from prefect_github import GitHubCredentials
from prefect_github.graphql import _execute_graphql_op
from prefect_github.schemas import graphql_schema
from sgqlc.operation import Operation


@task()
def create_pull_request(
    repository_id: str,
    base_ref_name: str,
    head_ref_name: str,
    title: str,
    github_credentials: GitHubCredentials,
    body: str = None,
    maintainer_can_modify: bool = None,
    draft: bool = None,
) -> Dict[str, Any]:
    """
    Create a new pull request.

    Args:
        repository_id: The Node ID of the repository.
        base_ref_name: The name of the branch you want your changes pulled
            into. This should be an existing branch on the current
            repository. You cannot update the base branch on a pull
            request to point to another repository.
        head_ref_name: The name of the branch where your changes are
            implemented. For cross-repository pull requests in the
            same network, namespace `head_ref_name` with a user like
            this: `username:branch`.
        title: The title of the pull request.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        body: The contents of the pull request.
        maintainer_can_modify: Indicates whether maintainers can modify the
            pull request.
        draft: Indicates whether this pull request should be a draft.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    _ = op.create_pull_request(
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

    result = _execute_graphql_op(op, github_credentials)
    return result
@task()
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
) -> Dict[str, Any]:
    """
    Creates a new issue.

    Args:
        repository_id: The Node ID of the repository.
        title: The title for the issue.
        assignee_ids: The Node ID for the user assignee for this issue.
        label_ids: An array of Node IDs of labels for this issue.
        project_ids: An array of Node IDs for projects associated with this
            issue.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        body: The body for the issue description.
        milestone_id: The Node ID of the milestone for this issue.
        issue_template: The name of an issue template in the repository,
            assigns labels and assignees from the template to the
            issue

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    _ = op.create_issue(
        input=dict(
            repository_id=repository_id,
            title=title,
            assignee_ids=assignee_ids,
            label_ids=label_ids,
            project_ids=project_ids,
            body=body,
            milestone_id=milestone_id,
            issue_template=issue_template,
        )
    )

    result = _execute_graphql_op(op, github_credentials)
    return result
@task()
def add_star(
    starrable_id: str,
    github_credentials: GitHubCredentials,
) -> Dict[str, Any]:
    """
    Adds a star to a Starrable.

    Args:
        starrable_id: The Starrable ID to star.
        github_credentials: github: Credentials to use for authentication with
            GitHub.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Mutation)
    _ = op.add_star(
        input=dict(
            starrable_id=starrable_id,
        )
    )

    result = _execute_graphql_op(op, github_credentials)
    return result
