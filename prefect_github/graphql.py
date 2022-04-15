from pprint import pformat
from typing import Union

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials


def _execute_graphql_op(
    op: Union[Operation, str], github_credentials: GitHubCredentials, **vars
):
    """
    Helper function for executing GraphQL operations.
    """
    endpoint = github_credentials.get_endpoint()
    result = endpoint(op, vars)
    if "errors" in result:
        errors = pformat(result["errors"])
        raise RuntimeError(f"Errors encountered:\n{errors}")
    return result["data"]


@task
def execute_graphql(
    op: Union[Operation, str], github_credentials: GitHubCredentials, **vars
):
    """
    Generic function for executing GraphQL operations.

    Args:
        op: The operation, either as a valid GraphQL string or sgqlc.Operation.
        github_credentials: Credentials to use for authentication with GitHub."

    Returns:
        A dict of the returned fields.
    """
    result = _execute_graphql_op(op, github_credentials, **vars)
    return result
