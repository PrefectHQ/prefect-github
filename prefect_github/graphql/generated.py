"""
This is a module containing generic GraphQL tasks
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended.

from pprint import pformat
from typing import Any, Dict, Iterable, List, Tuple, Union

from prefect import task
from prefect.utilities.asyncutils import run_sync_in_worker_thread
from sgqlc.operation import Operation, Selection

from prefect_github import GitHubCredentials
from prefect_github.utils import camel_to_snake_case


def _subset_return_fields(
    op_selection: Selection,
    op_stack: List[str],
    return_fields: Iterable[str],
    return_fields_defaults: Dict[Tuple, Tuple],
):
    """
    Helper function to subset return fields.
    """
    if not return_fields:
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    return_fields = tuple(
        camel_to_snake_case(return_field) for return_field in return_fields
    )

    try:
        op_selection.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_selection.nodes().__fields__(*return_fields)
    return op_selection


@task
async def execute_graphql(
    op: Union[Operation, str],
    github_credentials: GitHubCredentials,
    error_key: str = "errors",
    **vars,
) -> Dict[str, Any]:
    # NOTE: Maintainers can update these examples to match their collection!
    """
    Generic function for executing GraphQL operations.

    Args:
        op: The operation, either as a valid GraphQL string or sgqlc.Operation.
        github_credentials: Credentials to use for authentication with GitHub.
        error_key: The key name to look out for in the response
            that indicates an error has occurred with the request.

    Returns:
        A dict of the returned fields.

    Examples:
        Queries the first three issues from the Prefect repository
        using a string query.
        ```python
        from prefect import flow
        from prefect_github import GitHubCredentials
        from prefect_github.graphql import execute_graphql

        @flow()
        def example_execute_graphql_flow():
            op = '''
                query GitHubRepoIssues($owner: String!, $name: String!) {
                    repository(owner: $owner, name: $name) {
                        issues(last: 3) {
                            nodes {
                                number
                                title
                            }
                        }
                    }
                }
            '''
            token = "ghp_..."
            github_credentials = GitHubCredentials(token=token)
            params = dict(owner="PrefectHQ", name="Prefect")
            result = execute_graphql(op, github_credentials, **params)
            return result

        example_execute_graphql_flow()
        ```

        Queries the first three issues from Prefect repository
        using a sgqlc.Operation.
        ```python
        from prefect import flow
        from sgqlc.operation import Operation
        from prefect_github import GitHubCredentials
        from prefect_github.schemas import graphql_schema
        from prefect_github.graphql import execute_graphql

        @flow()
        def example_execute_graphql_flow():
            op = Operation(graphql_schema.Query)
            op_settings = op.repository(
                owner="PrefectHQ", name="Prefect"
            ).issues(
                first=3
            ).nodes()
            op_settings.__fields__("id", "title")
            token = "ghp_..."
            github_credentials = GitHubCredentials(token=token)
            result = execute_graphql(
                op,
                github_credentials,
            )
            return result

        example_execute_graphql_flow()
        ```
    """
    endpoint = github_credentials.get_endpoint()
    result = await run_sync_in_worker_thread(endpoint, op, vars)
    if error_key in result:
        errors = pformat(result[error_key])
        raise RuntimeError(f"Error encountered:\n{errors}")
    return result["data"]
