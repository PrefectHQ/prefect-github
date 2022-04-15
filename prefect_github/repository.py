"""
This is a module for interacting with GitHub Queryrepository tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials
from prefect_github.graphql import _execute_graphql_op
from prefect_github.schemas import graphql_schema
from prefect_github.utils import initialize_return_fields_defaults

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "repository.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task()
def query_repository(
    owner: str,
    name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The query root of GitHub's GraphQL interface.

    Args:
        owner: The login field of a user or organization
        name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        follow_renames: Follow repository renames. If disabled, a repository
            referenced by its old name will return an error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=owner,
        name=name,
        follow_renames=follow_renames,
    )
    if not return_fields:
        op_stack = tuple(["repository"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_project(
    repository_owner: str,
    repository_name: str,
    project_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Find project by number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        project_number: The project number to find.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).project(
        number=project_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "project"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_projects(
    repository_owner: str,
    repository_name: str,
    projects_states: List[graphql_schema.ProjectState],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    projects_order_by: graphql_schema.ProjectOrder = None,
    projects_search: str = None,
    projects_after: str = None,
    projects_before: str = None,
    projects_first: int = None,
    projects_last: int = None,
) -> Dict[str, Any]:
    """
    A list of projects under the owner.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        projects_states: A list of states to filter the projects by.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        projects_order_by: Ordering options for projects returned from the
            connection
        projects_search: Query to search projects by, currently only searching
            by name.
        projects_after: Returns the elements in the list that come after the
            specified cursor.
        projects_before: Returns the elements in the list that come before the
            specified cursor.
        projects_first: Returns the first _n_ elements from the list.
        projects_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).projects(
        states=projects_states,
        order_by=projects_order_by,
        search=projects_search,
        after=projects_after,
        before=projects_before,
        first=projects_first,
        last=projects_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "projects"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_packages(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    packages_after: str = None,
    packages_before: str = None,
    packages_first: int = None,
    packages_last: int = None,
    packages_names: str = None,
    packages_repository_id: str = None,
    packages_package_type: graphql_schema.PackageType = None,
    packages_order_by: graphql_schema.PackageOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    A list of packages under the owner.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        packages_after: Returns the elements in the list that come after the
            specified cursor.
        packages_before: Returns the elements in the list that come before the
            specified cursor.
        packages_first: Returns the first _n_ elements from the list.
        packages_last: Returns the last _n_ elements from the list.
        packages_names: Find packages by their names.
        packages_repository_id: Find packages in a repository by ID.
        packages_package_type: Filter registry package by type.
        packages_order_by: Ordering of the returned packages.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).packages(
        after=packages_after,
        before=packages_before,
        first=packages_first,
        last=packages_last,
        names=packages_names,
        repository_id=packages_repository_id,
        package_type=packages_package_type,
        order_by=packages_order_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "packages"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_stargazers(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    stargazers_after: str = None,
    stargazers_before: str = None,
    stargazers_first: int = None,
    stargazers_last: int = None,
    stargazers_order_by: graphql_schema.StarOrder = None,
) -> Dict[str, Any]:
    """
    A list of users who have starred this starrable.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        stargazers_after: Returns the elements in the list that come after the
            specified cursor.
        stargazers_before: Returns the elements in the list that come before
            the specified cursor.
        stargazers_first: Returns the first _n_ elements from the list.
        stargazers_last: Returns the last _n_ elements from the list.
        stargazers_order_by: Order for connection

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).stargazers(
        after=stargazers_after,
        before=stargazers_before,
        first=stargazers_first,
        last=stargazers_last,
        order_by=stargazers_order_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "stargazers"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_license_info(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The license associated with the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).license_info()
    if not return_fields:
        op_stack = tuple(["repository", "license_info"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_owner(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The User owner of the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).owner()
    if not return_fields:
        op_stack = tuple(["repository", "owner"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_assignable_users(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    assignable_users_query: str = None,
    assignable_users_after: str = None,
    assignable_users_before: str = None,
    assignable_users_first: int = None,
    assignable_users_last: int = None,
) -> Dict[str, Any]:
    """
    A list of users that can be assigned to issues in this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        assignable_users_query: Filters users with query on user name and
            login
        assignable_users_after: Returns the elements in the list that come
            after the specified cursor.
        assignable_users_before: Returns the elements in the list that come
            before the specified cursor.
        assignable_users_first: Returns the first _n_ elements from the list.
        assignable_users_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).assignable_users(
        query=assignable_users_query,
        after=assignable_users_after,
        before=assignable_users_before,
        first=assignable_users_first,
        last=assignable_users_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "assignable_users"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_branch_protection_rules(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    branch_protection_rules_after: str = None,
    branch_protection_rules_before: str = None,
    branch_protection_rules_first: int = None,
    branch_protection_rules_last: int = None,
) -> Dict[str, Any]:
    """
    A list of branch protection rules for this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        branch_protection_rules_after: Returns the elements in the list that
            come after the specified cursor.
        branch_protection_rules_before: Returns the elements in the list that
            come before the specified cursor.
        branch_protection_rules_first: Returns the first _n_ elements from the
            list.
        branch_protection_rules_last: Returns the last _n_ elements from the
            list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).branch_protection_rules(
        after=branch_protection_rules_after,
        before=branch_protection_rules_before,
        first=branch_protection_rules_first,
        last=branch_protection_rules_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "branch_protection_rules"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_code_of_conduct(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns the code of conduct for this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).code_of_conduct()
    if not return_fields:
        op_stack = tuple(["repository", "code_of_conduct"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_collaborators(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    collaborators_affiliation: graphql_schema.CollaboratorAffiliation = None,
    collaborators_query: str = None,
    collaborators_after: str = None,
    collaborators_before: str = None,
    collaborators_first: int = None,
    collaborators_last: int = None,
) -> Dict[str, Any]:
    """
    A list of collaborators associated with the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        collaborators_affiliation: Collaborators affiliation level with a
            repository.
        collaborators_query: Filters users with query on user name and login
        collaborators_after: Returns the elements in the list that come after
            the specified cursor.
        collaborators_before: Returns the elements in the list that come
            before the specified cursor.
        collaborators_first: Returns the first _n_ elements from the list.
        collaborators_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).collaborators(
        affiliation=collaborators_affiliation,
        query=collaborators_query,
        after=collaborators_after,
        before=collaborators_before,
        first=collaborators_first,
        last=collaborators_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "collaborators"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_commit_comments(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    commit_comments_after: str = None,
    commit_comments_before: str = None,
    commit_comments_first: int = None,
    commit_comments_last: int = None,
) -> Dict[str, Any]:
    """
    A list of commit comments associated with the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        commit_comments_after: Returns the elements in the list that come
            after the specified cursor.
        commit_comments_before: Returns the elements in the list that come
            before the specified cursor.
        commit_comments_first: Returns the first _n_ elements from the list.
        commit_comments_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).commit_comments(
        after=commit_comments_after,
        before=commit_comments_before,
        first=commit_comments_first,
        last=commit_comments_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "commit_comments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_contact_links(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a list of contact links associated to the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).contact_links()
    if not return_fields:
        op_stack = tuple(["repository", "contact_links"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_default_branch_ref(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The Ref associated with the repository's default branch.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).default_branch_ref()
    if not return_fields:
        op_stack = tuple(["repository", "default_branch_ref"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_deploy_keys(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    deploy_keys_after: str = None,
    deploy_keys_before: str = None,
    deploy_keys_first: int = None,
    deploy_keys_last: int = None,
) -> Dict[str, Any]:
    """
    A list of deploy keys that are on this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        deploy_keys_after: Returns the elements in the list that come after
            the specified cursor.
        deploy_keys_before: Returns the elements in the list that come before
            the specified cursor.
        deploy_keys_first: Returns the first _n_ elements from the list.
        deploy_keys_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).deploy_keys(
        after=deploy_keys_after,
        before=deploy_keys_before,
        first=deploy_keys_first,
        last=deploy_keys_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "deploy_keys"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_deployments(
    repository_owner: str,
    repository_name: str,
    deployments_environments: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    deployments_order_by: graphql_schema.DeploymentOrder = {
        "field": "CREATED_AT",
        "direction": "ASC",
    },
    deployments_after: str = None,
    deployments_before: str = None,
    deployments_first: int = None,
    deployments_last: int = None,
) -> Dict[str, Any]:
    """
    Deployments associated with the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        deployments_environments: Environments to list deployments for
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        deployments_order_by: Ordering options for deployments returned from
            the connection.
        deployments_after: Returns the elements in the list that come after
            the specified cursor.
        deployments_before: Returns the elements in the list that come before
            the specified cursor.
        deployments_first: Returns the first _n_ elements from the list.
        deployments_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).deployments(
        environments=deployments_environments,
        order_by=deployments_order_by,
        after=deployments_after,
        before=deployments_before,
        first=deployments_first,
        last=deployments_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "deployments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_discussion(
    repository_owner: str,
    repository_name: str,
    discussion_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single discussion from the current repository by number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        discussion_number: The number for the discussion to be returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).discussion(
        number=discussion_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "discussion"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_discussion_categories(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    discussion_categories_after: str = None,
    discussion_categories_before: str = None,
    discussion_categories_first: int = None,
    discussion_categories_last: int = None,
    discussion_categories_filter_by_assignable: bool = False,
) -> Dict[str, Any]:
    """
    A list of discussion categories that are available in the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        discussion_categories_after: Returns the elements in the list that
            come after the specified cursor.
        discussion_categories_before: Returns the elements in the list that
            come before the specified cursor.
        discussion_categories_first: Returns the first _n_ elements from the
            list.
        discussion_categories_last: Returns the last _n_ elements from the
            list.
        discussion_categories_filter_by_assignable: Filter by categories that
            are assignable by the viewer.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).discussion_categories(
        after=discussion_categories_after,
        before=discussion_categories_before,
        first=discussion_categories_first,
        last=discussion_categories_last,
        filter_by_assignable=discussion_categories_filter_by_assignable,
    )
    if not return_fields:
        op_stack = tuple(["repository", "discussion_categories"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_discussions(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    discussions_after: str = None,
    discussions_before: str = None,
    discussions_first: int = None,
    discussions_last: int = None,
    discussions_category_id: str = None,
    discussions_order_by: graphql_schema.DiscussionOrder = {
        "field": "UPDATED_AT",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    A list of discussions that have been opened in the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        discussions_after: Returns the elements in the list that come after
            the specified cursor.
        discussions_before: Returns the elements in the list that come before
            the specified cursor.
        discussions_first: Returns the first _n_ elements from the list.
        discussions_last: Returns the last _n_ elements from the list.
        discussions_category_id: Only include discussions that belong to the
            category with this ID.
        discussions_order_by: Ordering options for discussions returned from
            the connection.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).discussions(
        after=discussions_after,
        before=discussions_before,
        first=discussions_first,
        last=discussions_last,
        category_id=discussions_category_id,
        order_by=discussions_order_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "discussions"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_environment(
    repository_owner: str,
    repository_name: str,
    environment_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single active environment from the current repository by name.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        environment_name: The name of the environment to be returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).environment(
        name=environment_name,
    )
    if not return_fields:
        op_stack = tuple(["repository", "environment"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_environments(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    environments_after: str = None,
    environments_before: str = None,
    environments_first: int = None,
    environments_last: int = None,
) -> Dict[str, Any]:
    """
    A list of environments that are in this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        environments_after: Returns the elements in the list that come after
            the specified cursor.
        environments_before: Returns the elements in the list that come before
            the specified cursor.
        environments_first: Returns the first _n_ elements from the list.
        environments_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).environments(
        after=environments_after,
        before=environments_before,
        first=environments_first,
        last=environments_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "environments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_forks(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    forks_privacy: graphql_schema.RepositoryPrivacy = None,
    forks_order_by: graphql_schema.RepositoryOrder = None,
    forks_affiliations: List[graphql_schema.RepositoryAffiliation] = None,
    forks_owner_affiliations: List[graphql_schema.RepositoryAffiliation] = [
        "OWNER",
        "COLLABORATOR",
    ],
    forks_is_locked: bool = None,
    forks_after: str = None,
    forks_before: str = None,
    forks_first: int = None,
    forks_last: int = None,
) -> Dict[str, Any]:
    """
    A list of direct forked repositories.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        forks_privacy: If non-null, filters repositories according to privacy
        forks_order_by: Ordering options for repositories returned from the
            connection
        forks_affiliations: Array of viewer's affiliation options for
            repositories returned from the connection. For example,
            OWNER will include only repositories that the current
            viewer owns.
        forks_owner_affiliations: Array of owner's affiliation options for
            repositories returned from the connection. For example,
            OWNER will include only repositories that the organization
            or user being viewed owns.
        forks_is_locked: If non-null, filters repositories according to
            whether they have been locked
        forks_after: Returns the elements in the list that come after the
            specified cursor.
        forks_before: Returns the elements in the list that come before the
            specified cursor.
        forks_first: Returns the first _n_ elements from the list.
        forks_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).forks(
        privacy=forks_privacy,
        order_by=forks_order_by,
        affiliations=forks_affiliations,
        owner_affiliations=forks_owner_affiliations,
        is_locked=forks_is_locked,
        after=forks_after,
        before=forks_before,
        first=forks_first,
        last=forks_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "forks"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_funding_links(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The funding links for this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).funding_links()
    if not return_fields:
        op_stack = tuple(["repository", "funding_links"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_interaction_ability(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The interaction ability settings for this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).interaction_ability()
    if not return_fields:
        op_stack = tuple(["repository", "interaction_ability"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_issue(
    repository_owner: str,
    repository_name: str,
    issue_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single issue from the current repository by number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        issue_number: The number for the issue to be returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issue(
        number=issue_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "issue"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_issue_or_pull_request(
    repository_owner: str,
    repository_name: str,
    issue_or_pull_request_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single issue-like object from the current repository by number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        issue_or_pull_request_number: The number for the issue to be returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issue_or_pull_request(
        number=issue_or_pull_request_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "issue_or_pull_request"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_issue_templates(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a list of issue templates associated to the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issue_templates()
    if not return_fields:
        op_stack = tuple(["repository", "issue_templates"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_issues(
    repository_owner: str,
    repository_name: str,
    issues_labels: str,
    issues_states: List[graphql_schema.IssueState],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    issues_order_by: graphql_schema.IssueOrder = None,
    issues_filter_by: graphql_schema.IssueFilters = None,
    issues_after: str = None,
    issues_before: str = None,
    issues_first: int = None,
    issues_last: int = None,
) -> Dict[str, Any]:
    """
    A list of issues that have been opened in the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        issues_labels: A list of label names to filter the pull requests by.
        issues_states: A list of states to filter the issues by.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        issues_order_by: Ordering options for issues returned from the
            connection.
        issues_filter_by: Filtering options for issues returned from the
            connection.
        issues_after: Returns the elements in the list that come after the
            specified cursor.
        issues_before: Returns the elements in the list that come before the
            specified cursor.
        issues_first: Returns the first _n_ elements from the list.
        issues_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issues(
        labels=issues_labels,
        states=issues_states,
        order_by=issues_order_by,
        filter_by=issues_filter_by,
        after=issues_after,
        before=issues_before,
        first=issues_first,
        last=issues_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "issues"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_label(
    repository_owner: str,
    repository_name: str,
    label_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single label by name.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        label_name: Label name
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).label(
        name=label_name,
    )
    if not return_fields:
        op_stack = tuple(["repository", "label"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_labels(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    labels_order_by: graphql_schema.LabelOrder = {
        "field": "CREATED_AT",
        "direction": "ASC",
    },
    labels_after: str = None,
    labels_before: str = None,
    labels_first: int = None,
    labels_last: int = None,
    labels_query: str = None,
) -> Dict[str, Any]:
    """
    A list of labels associated with the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        labels_order_by: Ordering options for labels returned from the
            connection.
        labels_after: Returns the elements in the list that come after the
            specified cursor.
        labels_before: Returns the elements in the list that come before the
            specified cursor.
        labels_first: Returns the first _n_ elements from the list.
        labels_last: Returns the last _n_ elements from the list.
        labels_query: If provided, searches labels by name and description.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).labels(
        order_by=labels_order_by,
        after=labels_after,
        before=labels_before,
        first=labels_first,
        last=labels_last,
        query=labels_query,
    )
    if not return_fields:
        op_stack = tuple(["repository", "labels"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_languages(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    languages_after: str = None,
    languages_before: str = None,
    languages_first: int = None,
    languages_last: int = None,
    languages_order_by: graphql_schema.LanguageOrder = None,
) -> Dict[str, Any]:
    """
    A list containing a breakdown of the language composition of the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        languages_after: Returns the elements in the list that come after the
            specified cursor.
        languages_before: Returns the elements in the list that come before
            the specified cursor.
        languages_first: Returns the first _n_ elements from the list.
        languages_last: Returns the last _n_ elements from the list.
        languages_order_by: Order for connection

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).languages(
        after=languages_after,
        before=languages_before,
        first=languages_first,
        last=languages_last,
        order_by=languages_order_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "languages"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_latest_release(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Get the latest release for the repository if one exists.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).latest_release()
    if not return_fields:
        op_stack = tuple(["repository", "latest_release"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_mentionable_users(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    mentionable_users_query: str = None,
    mentionable_users_after: str = None,
    mentionable_users_before: str = None,
    mentionable_users_first: int = None,
    mentionable_users_last: int = None,
) -> Dict[str, Any]:
    """
    A list of Users that can be mentioned in the context of the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        mentionable_users_query: Filters users with query on user name and
            login
        mentionable_users_after: Returns the elements in the list that come
            after the specified cursor.
        mentionable_users_before: Returns the elements in the list that come
            before the specified cursor.
        mentionable_users_first: Returns the first _n_ elements from the list.
        mentionable_users_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).mentionable_users(
        query=mentionable_users_query,
        after=mentionable_users_after,
        before=mentionable_users_before,
        first=mentionable_users_first,
        last=mentionable_users_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "mentionable_users"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_milestone(
    repository_owner: str,
    repository_name: str,
    milestone_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single milestone from the current repository by number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        milestone_number: The number for the milestone to be returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).milestone(
        number=milestone_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "milestone"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_milestones(
    repository_owner: str,
    repository_name: str,
    milestones_states: List[graphql_schema.MilestoneState],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    milestones_after: str = None,
    milestones_before: str = None,
    milestones_first: int = None,
    milestones_last: int = None,
    milestones_order_by: graphql_schema.MilestoneOrder = None,
    milestones_query: str = None,
) -> Dict[str, Any]:
    """
    A list of milestones associated with the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        milestones_states: Filter by the state of the milestones.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        milestones_after: Returns the elements in the list that come after the
            specified cursor.
        milestones_before: Returns the elements in the list that come before
            the specified cursor.
        milestones_first: Returns the first _n_ elements from the list.
        milestones_last: Returns the last _n_ elements from the list.
        milestones_order_by: Ordering options for milestones.
        milestones_query: Filters milestones with a query on the title

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).milestones(
        states=milestones_states,
        after=milestones_after,
        before=milestones_before,
        first=milestones_first,
        last=milestones_last,
        order_by=milestones_order_by,
        query=milestones_query,
    )
    if not return_fields:
        op_stack = tuple(["repository", "milestones"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_object(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    object_oid: datetime = None,
    object_expression: str = None,
) -> Dict[str, Any]:
    """
    A Git object in the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        object_oid: The Git object ID
        object_expression: A Git revision expression suitable for rev-parse

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).object(
        oid=object_oid,
        expression=object_expression,
    )
    if not return_fields:
        op_stack = tuple(["repository", "object"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_pinned_discussions(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    pinned_discussions_after: str = None,
    pinned_discussions_before: str = None,
    pinned_discussions_first: int = None,
    pinned_discussions_last: int = None,
) -> Dict[str, Any]:
    """
    A list of discussions that have been pinned in this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        pinned_discussions_after: Returns the elements in the list that come
            after the specified cursor.
        pinned_discussions_before: Returns the elements in the list that come
            before the specified cursor.
        pinned_discussions_first: Returns the first _n_ elements from the
            list.
        pinned_discussions_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).pinned_discussions(
        after=pinned_discussions_after,
        before=pinned_discussions_before,
        first=pinned_discussions_first,
        last=pinned_discussions_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "pinned_discussions"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_pinned_issues(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    pinned_issues_after: str = None,
    pinned_issues_before: str = None,
    pinned_issues_first: int = None,
    pinned_issues_last: int = None,
) -> Dict[str, Any]:
    """
    A list of pinned issues for this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        pinned_issues_after: Returns the elements in the list that come after
            the specified cursor.
        pinned_issues_before: Returns the elements in the list that come
            before the specified cursor.
        pinned_issues_first: Returns the first _n_ elements from the list.
        pinned_issues_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).pinned_issues(
        after=pinned_issues_after,
        before=pinned_issues_before,
        first=pinned_issues_first,
        last=pinned_issues_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "pinned_issues"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_primary_language(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    The primary language of the repository's code.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).primary_language()
    if not return_fields:
        op_stack = tuple(["repository", "primary_language"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_project_next(
    repository_owner: str,
    repository_name: str,
    project_next_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Finds and returns the Project (beta) according to the provided Project (beta)
    number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        project_next_number: The ProjectNext number.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).project_next(
        number=project_next_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "project_next"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_projects_next(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    projects_next_after: str = None,
    projects_next_before: str = None,
    projects_next_first: int = None,
    projects_next_last: int = None,
    projects_next_query: str = None,
    projects_next_sort_by: graphql_schema.ProjectNextOrderField = "TITLE",
) -> Dict[str, Any]:
    """
    List of projects (beta) linked to this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        projects_next_after: Returns the elements in the list that come after
            the specified cursor.
        projects_next_before: Returns the elements in the list that come
            before the specified cursor.
        projects_next_first: Returns the first _n_ elements from the list.
        projects_next_last: Returns the last _n_ elements from the list.
        projects_next_query: A project (beta) to search for linked to the
            repo.
        projects_next_sort_by: How to order the returned project (beta)
            objects.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).projects_next(
        after=projects_next_after,
        before=projects_next_before,
        first=projects_next_first,
        last=projects_next_last,
        query=projects_next_query,
        sort_by=projects_next_sort_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "projects_next"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_pull_request(
    repository_owner: str,
    repository_name: str,
    pull_request_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a single pull request from the current repository by number.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        pull_request_number: The number for the pull request to be returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).pull_request(
        number=pull_request_number,
    )
    if not return_fields:
        op_stack = tuple(["repository", "pull_request"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_pull_request_templates(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Returns a list of pull request templates associated to the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).pull_request_templates()
    if not return_fields:
        op_stack = tuple(["repository", "pull_request_templates"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_pull_requests(
    repository_owner: str,
    repository_name: str,
    pull_requests_states: List[graphql_schema.PullRequestState],
    pull_requests_labels: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    pull_requests_head_ref_name: str = None,
    pull_requests_base_ref_name: str = None,
    pull_requests_order_by: graphql_schema.IssueOrder = None,
    pull_requests_after: str = None,
    pull_requests_before: str = None,
    pull_requests_first: int = None,
    pull_requests_last: int = None,
) -> Dict[str, Any]:
    """
    A list of pull requests that have been opened in the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        pull_requests_states: A list of states to filter the pull requests by.
        pull_requests_labels: A list of label names to filter the pull
            requests by.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        pull_requests_head_ref_name: The head ref name to filter the pull
            requests by.
        pull_requests_base_ref_name: The base ref name to filter the pull
            requests by.
        pull_requests_order_by: Ordering options for pull requests returned
            from the connection.
        pull_requests_after: Returns the elements in the list that come after
            the specified cursor.
        pull_requests_before: Returns the elements in the list that come
            before the specified cursor.
        pull_requests_first: Returns the first _n_ elements from the list.
        pull_requests_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).pull_requests(
        states=pull_requests_states,
        labels=pull_requests_labels,
        head_ref_name=pull_requests_head_ref_name,
        base_ref_name=pull_requests_base_ref_name,
        order_by=pull_requests_order_by,
        after=pull_requests_after,
        before=pull_requests_before,
        first=pull_requests_first,
        last=pull_requests_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "pull_requests"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_ref(
    repository_owner: str,
    repository_name: str,
    ref_qualified_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Fetch a given ref from the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        ref_qualified_name: The ref to retrieve. Fully qualified matches are
            checked in order (`refs/heads/master`) before falling back
            onto checks for short name matches (`master`).
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).ref(
        qualified_name=ref_qualified_name,
    )
    if not return_fields:
        op_stack = tuple(["repository", "ref"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_refs(
    repository_owner: str,
    repository_name: str,
    refs_ref_prefix: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    refs_query: str = None,
    refs_after: str = None,
    refs_before: str = None,
    refs_first: int = None,
    refs_last: int = None,
    refs_direction: graphql_schema.OrderDirection = None,
    refs_order_by: graphql_schema.RefOrder = None,
) -> Dict[str, Any]:
    """
    Fetch a list of refs from the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        refs_ref_prefix: A ref name prefix like `refs/heads/`, `refs/tags/`,
            etc.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        refs_query: Filters refs with query on name
        refs_after: Returns the elements in the list that come after the
            specified cursor.
        refs_before: Returns the elements in the list that come before the
            specified cursor.
        refs_first: Returns the first _n_ elements from the list.
        refs_last: Returns the last _n_ elements from the list.
        refs_direction: DEPRECATED: use orderBy. The ordering direction.
        refs_order_by: Ordering options for refs returned from the connection.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).refs(
        ref_prefix=refs_ref_prefix,
        query=refs_query,
        after=refs_after,
        before=refs_before,
        first=refs_first,
        last=refs_last,
        direction=refs_direction,
        order_by=refs_order_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "refs"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_release(
    repository_owner: str,
    repository_name: str,
    release_tag_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Lookup a single release given various criteria.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        release_tag_name: The name of the Tag the Release was created from
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).release(
        tag_name=release_tag_name,
    )
    if not return_fields:
        op_stack = tuple(["repository", "release"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_releases(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    releases_after: str = None,
    releases_before: str = None,
    releases_first: int = None,
    releases_last: int = None,
    releases_order_by: graphql_schema.ReleaseOrder = None,
) -> Dict[str, Any]:
    """
    List of releases which are dependent on this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        releases_after: Returns the elements in the list that come after the
            specified cursor.
        releases_before: Returns the elements in the list that come before the
            specified cursor.
        releases_first: Returns the first _n_ elements from the list.
        releases_last: Returns the last _n_ elements from the list.
        releases_order_by: Order for connection

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).releases(
        after=releases_after,
        before=releases_before,
        first=releases_first,
        last=releases_last,
        order_by=releases_order_by,
    )
    if not return_fields:
        op_stack = tuple(["repository", "releases"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_repository_topics(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    repository_topics_after: str = None,
    repository_topics_before: str = None,
    repository_topics_first: int = None,
    repository_topics_last: int = None,
) -> Dict[str, Any]:
    """
    A list of applied repository-topic associations for this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        repository_topics_after: Returns the elements in the list that come
            after the specified cursor.
        repository_topics_before: Returns the elements in the list that come
            before the specified cursor.
        repository_topics_first: Returns the first _n_ elements from the list.
        repository_topics_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).repository_topics(
        after=repository_topics_after,
        before=repository_topics_before,
        first=repository_topics_first,
        last=repository_topics_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "repository_topics"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_submodules(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    submodules_after: str = None,
    submodules_before: str = None,
    submodules_first: int = None,
    submodules_last: int = None,
) -> Dict[str, Any]:
    """
    Returns a list of all submodules in this repository parsed from the .gitmodules
    file as of the default branch's HEAD commit.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        submodules_after: Returns the elements in the list that come after the
            specified cursor.
        submodules_before: Returns the elements in the list that come before
            the specified cursor.
        submodules_first: Returns the first _n_ elements from the list.
        submodules_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).submodules(
        after=submodules_after,
        before=submodules_before,
        first=submodules_first,
        last=submodules_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "submodules"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_vulnerability_alerts(
    repository_owner: str,
    repository_name: str,
    vulnerability_alerts_states: List[graphql_schema.RepositoryVulnerabilityAlertState],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    vulnerability_alerts_after: str = None,
    vulnerability_alerts_before: str = None,
    vulnerability_alerts_first: int = None,
    vulnerability_alerts_last: int = None,
) -> Dict[str, Any]:
    """
    A list of vulnerability alerts that are on this repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        vulnerability_alerts_states: Filter by the state of the alert
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        vulnerability_alerts_after: Returns the elements in the list that come
            after the specified cursor.
        vulnerability_alerts_before: Returns the elements in the list that
            come before the specified cursor.
        vulnerability_alerts_first: Returns the first _n_ elements from the
            list.
        vulnerability_alerts_last: Returns the last _n_ elements from the
            list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).vulnerability_alerts(
        states=vulnerability_alerts_states,
        after=vulnerability_alerts_after,
        before=vulnerability_alerts_before,
        first=vulnerability_alerts_first,
        last=vulnerability_alerts_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "vulnerability_alerts"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_repository_watchers(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
    watchers_after: str = None,
    watchers_before: str = None,
    watchers_first: int = None,
    watchers_last: int = None,
) -> Dict[str, Any]:
    """
    A list of users watching the repository.

    Args:
        repository_owner: The login field of a user or organization
        repository_name: The name of the repository
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an
            error.
        watchers_after: Returns the elements in the list that come after the
            specified cursor.
        watchers_before: Returns the elements in the list that come before the
            specified cursor.
        watchers_first: Returns the first _n_ elements from the list.
        watchers_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).watchers(
        after=watchers_after,
        before=watchers_before,
        first=watchers_first,
        last=watchers_last,
    )
    if not return_fields:
        op_stack = tuple(["repository", "watchers"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result
