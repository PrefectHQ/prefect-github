"""
This is a module for interacting with GitHub Queryuser tasks.
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

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "user.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task()
def query_user(
    login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    The query root of GitHub's GraphQL interface.

    Args:
        login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=login,
    )
    if not return_fields:
        op_stack = tuple(["user"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_packages(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
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
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
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
    op_settings = op.user(login=user_login,).packages(
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
        op_stack = tuple(["user", "packages"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_project(
    user_login: str,
    project_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    Find project by number.

    Args:
        user_login: The user's login.
        project_number: The project number to find.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).project(
        number=project_number,
    )
    if not return_fields:
        op_stack = tuple(["user", "project"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_projects(
    user_login: str,
    projects_states: List[graphql_schema.ProjectState],
    github_credentials: GitHubCredentials,
    *return_fields: str,
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
        user_login: The user's login.
        projects_states: A list of states to filter the projects by.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
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
    op_settings = op.user(login=user_login,).projects(
        states=projects_states,
        order_by=projects_order_by,
        search=projects_search,
        after=projects_after,
        before=projects_before,
        first=projects_first,
        last=projects_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "projects"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_project_next(
    user_login: str,
    project_next_number: int,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    Find a project by project (beta) number.

    Args:
        user_login: The user's login.
        project_next_number: The project (beta) number.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).project_next(
        number=project_next_number,
    )
    if not return_fields:
        op_stack = tuple(["user", "project_next"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_projects_next(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    projects_next_after: str = None,
    projects_next_before: str = None,
    projects_next_first: int = None,
    projects_next_last: int = None,
    projects_next_query: str = None,
    projects_next_sort_by: graphql_schema.ProjectNextOrderField = "TITLE",
) -> Dict[str, Any]:
    """
    A list of projects (beta) under the owner.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        projects_next_after: Returns the elements in the list that come after
            the specified cursor.
        projects_next_before: Returns the elements in the list that come
            before the specified cursor.
        projects_next_first: Returns the first _n_ elements from the list.
        projects_next_last: Returns the last _n_ elements from the list.
        projects_next_query: A project (beta) to search for under the the
            owner.
        projects_next_sort_by: How to order the returned projects (beta).

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).projects_next(
        after=projects_next_after,
        before=projects_next_before,
        first=projects_next_first,
        last=projects_next_last,
        query=projects_next_query,
        sort_by=projects_next_sort_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "projects_next"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_repository_discussions(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_discussions_after: str = None,
    repository_discussions_before: str = None,
    repository_discussions_first: int = None,
    repository_discussions_last: int = None,
    repository_discussions_order_by: graphql_schema.DiscussionOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
    repository_discussions_repository_id: str = None,
    repository_discussions_answered: bool = None,
) -> Dict[str, Any]:
    """
    Discussions this user has started.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_discussions_after: Returns the elements in the list that
            come after the specified cursor.
        repository_discussions_before: Returns the elements in the list that
            come before the specified cursor.
        repository_discussions_first: Returns the first _n_ elements from the
            list.
        repository_discussions_last: Returns the last _n_ elements from the
            list.
        repository_discussions_order_by: Ordering options for discussions
            returned from the connection.
        repository_discussions_repository_id: Filter discussions to only those
            in a specific repository.
        repository_discussions_answered: Filter discussions to only those that
            have been answered or not. Defaults to including both
            answered and unanswered discussions.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).repository_discussions(
        after=repository_discussions_after,
        before=repository_discussions_before,
        first=repository_discussions_first,
        last=repository_discussions_last,
        order_by=repository_discussions_order_by,
        repository_id=repository_discussions_repository_id,
        answered=repository_discussions_answered,
    )
    if not return_fields:
        op_stack = tuple(["user", "repository_discussions"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_repository_discussion_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_discussion_comments_after: str = None,
    repository_discussion_comments_before: str = None,
    repository_discussion_comments_first: int = None,
    repository_discussion_comments_last: int = None,
    repository_discussion_comments_repository_id: str = None,
    repository_discussion_comments_only_answers: bool = False,
) -> Dict[str, Any]:
    """
    Discussion comments this user has authored.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repository_discussion_comments_after: Returns the elements in the list
            that come after the specified cursor.
        repository_discussion_comments_before: Returns the elements in the
            list that come before the specified cursor.
        repository_discussion_comments_first: Returns the first _n_ elements
            from the list.
        repository_discussion_comments_last: Returns the last _n_ elements
            from the list.
        repository_discussion_comments_repository_id: Filter discussion
            comments to only those in a specific repository.
        repository_discussion_comments_only_answers: Filter discussion
            comments to only those that were marked as the answer

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).repository_discussion_comments(
        after=repository_discussion_comments_after,
        before=repository_discussion_comments_before,
        first=repository_discussion_comments_first,
        last=repository_discussion_comments_last,
        repository_id=repository_discussion_comments_repository_id,
        only_answers=repository_discussion_comments_only_answers,
    )
    if not return_fields:
        op_stack = tuple(["user", "repository_discussion_comments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_repositories(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repositories_privacy: graphql_schema.RepositoryPrivacy = None,
    repositories_order_by: graphql_schema.RepositoryOrder = None,
    repositories_affiliations: List[graphql_schema.RepositoryAffiliation] = None,
    repositories_owner_affiliations: List[graphql_schema.RepositoryAffiliation] = [
        "OWNER",
        "COLLABORATOR",
    ],
    repositories_is_locked: bool = None,
    repositories_after: str = None,
    repositories_before: str = None,
    repositories_first: int = None,
    repositories_last: int = None,
    repositories_is_fork: bool = None,
) -> Dict[str, Any]:
    """
    A list of repositories that the user owns.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repositories_privacy: If non-null, filters repositories according to
            privacy
        repositories_order_by: Ordering options for repositories returned from
            the connection
        repositories_affiliations: Array of viewer's affiliation options for
            repositories returned from the connection. For example,
            OWNER will include only repositories that the current
            viewer owns.
        repositories_owner_affiliations: Array of owner's affiliation options
            for repositories returned from the connection. For
            example, OWNER will include only repositories that the
            organization or user being viewed owns.
        repositories_is_locked: If non-null, filters repositories according to
            whether they have been locked
        repositories_after: Returns the elements in the list that come after
            the specified cursor.
        repositories_before: Returns the elements in the list that come before
            the specified cursor.
        repositories_first: Returns the first _n_ elements from the list.
        repositories_last: Returns the last _n_ elements from the list.
        repositories_is_fork: If non-null, filters repositories according to
            whether they are forks of another repository

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).repositories(
        privacy=repositories_privacy,
        order_by=repositories_order_by,
        affiliations=repositories_affiliations,
        owner_affiliations=repositories_owner_affiliations,
        is_locked=repositories_is_locked,
        after=repositories_after,
        before=repositories_before,
        first=repositories_first,
        last=repositories_last,
        is_fork=repositories_is_fork,
    )
    if not return_fields:
        op_stack = tuple(["user", "repositories"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_repository(
    user_login: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repository_follow_renames: bool = True,
) -> Dict[str, Any]:
    """
    Find Repository.

    Args:
        user_login: The user's login.
        repository_name: Name of Repository to find.
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
    op_settings = op.user(login=user_login,).repository(
        name=repository_name,
        follow_renames=repository_follow_renames,
    )
    if not return_fields:
        op_stack = tuple(["user", "repository"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_item_showcase(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    Showcases a selection of repositories and gists that the profile owner has
    either curated or that have been selected automatically based on popularity.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=user_login,
    ).item_showcase()
    if not return_fields:
        op_stack = tuple(["user", "item_showcase"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_pinnable_items(
    user_login: str,
    pinnable_items_types: List[graphql_schema.PinnableItemType],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    pinnable_items_after: str = None,
    pinnable_items_before: str = None,
    pinnable_items_first: int = None,
    pinnable_items_last: int = None,
) -> Dict[str, Any]:
    """
    A list of repositories and gists this profile owner can pin to their profile.

    Args:
        user_login: The user's login.
        pinnable_items_types: Filter the types of pinnable items that are
            returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        pinnable_items_after: Returns the elements in the list that come after
            the specified cursor.
        pinnable_items_before: Returns the elements in the list that come
            before the specified cursor.
        pinnable_items_first: Returns the first _n_ elements from the list.
        pinnable_items_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).pinnable_items(
        types=pinnable_items_types,
        after=pinnable_items_after,
        before=pinnable_items_before,
        first=pinnable_items_first,
        last=pinnable_items_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "pinnable_items"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_pinned_items(
    user_login: str,
    pinned_items_types: List[graphql_schema.PinnableItemType],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    pinned_items_after: str = None,
    pinned_items_before: str = None,
    pinned_items_first: int = None,
    pinned_items_last: int = None,
) -> Dict[str, Any]:
    """
    A list of repositories and gists this profile owner has pinned to their profile.

    Args:
        user_login: The user's login.
        pinned_items_types: Filter the types of pinned items that are
            returned.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        pinned_items_after: Returns the elements in the list that come after
            the specified cursor.
        pinned_items_before: Returns the elements in the list that come before
            the specified cursor.
        pinned_items_first: Returns the first _n_ elements from the list.
        pinned_items_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).pinned_items(
        types=pinned_items_types,
        after=pinned_items_after,
        before=pinned_items_before,
        first=pinned_items_first,
        last=pinned_items_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "pinned_items"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsoring(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    sponsoring_after: str = None,
    sponsoring_before: str = None,
    sponsoring_first: int = None,
    sponsoring_last: int = None,
    sponsoring_order_by: graphql_schema.SponsorOrder = {
        "field": "RELEVANCE",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    List of users and organizations this entity is sponsoring.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        sponsoring_after: Returns the elements in the list that come after the
            specified cursor.
        sponsoring_before: Returns the elements in the list that come before
            the specified cursor.
        sponsoring_first: Returns the first _n_ elements from the list.
        sponsoring_last: Returns the last _n_ elements from the list.
        sponsoring_order_by: Ordering options for the users and organizations
            returned from the connection.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).sponsoring(
        after=sponsoring_after,
        before=sponsoring_before,
        first=sponsoring_first,
        last=sponsoring_last,
        order_by=sponsoring_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "sponsoring"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsors(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    sponsors_after: str = None,
    sponsors_before: str = None,
    sponsors_first: int = None,
    sponsors_last: int = None,
    sponsors_tier_id: str = None,
    sponsors_order_by: graphql_schema.SponsorOrder = {
        "field": "RELEVANCE",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    List of sponsors for this user or organization.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        sponsors_after: Returns the elements in the list that come after the
            specified cursor.
        sponsors_before: Returns the elements in the list that come before the
            specified cursor.
        sponsors_first: Returns the first _n_ elements from the list.
        sponsors_last: Returns the last _n_ elements from the list.
        sponsors_tier_id: If given, will filter for sponsors at the given
            tier. Will only return sponsors whose tier the viewer is
            permitted to see.
        sponsors_order_by: Ordering options for sponsors returned from the
            connection.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).sponsors(
        after=sponsors_after,
        before=sponsors_before,
        first=sponsors_first,
        last=sponsors_last,
        tier_id=sponsors_tier_id,
        order_by=sponsors_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "sponsors"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsors_activities(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    sponsors_activities_after: str = None,
    sponsors_activities_before: str = None,
    sponsors_activities_first: int = None,
    sponsors_activities_last: int = None,
    sponsors_activities_period: graphql_schema.SponsorsActivityPeriod = "MONTH",
    sponsors_activities_order_by: graphql_schema.SponsorsActivityOrder = {
        "field": "TIMESTAMP",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    Events involving this sponsorable, such as new sponsorships.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        sponsors_activities_after: Returns the elements in the list that come
            after the specified cursor.
        sponsors_activities_before: Returns the elements in the list that come
            before the specified cursor.
        sponsors_activities_first: Returns the first _n_ elements from the
            list.
        sponsors_activities_last: Returns the last _n_ elements from the list.
        sponsors_activities_period: Filter activities returned to only those
            that occurred in a given time range.
        sponsors_activities_order_by: Ordering options for activity returned
            from the connection.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).sponsors_activities(
        after=sponsors_activities_after,
        before=sponsors_activities_before,
        first=sponsors_activities_first,
        last=sponsors_activities_last,
        period=sponsors_activities_period,
        order_by=sponsors_activities_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "sponsors_activities"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsors_listing(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    The GitHub Sponsors listing for this user or organization.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=user_login,
    ).sponsors_listing()
    if not return_fields:
        op_stack = tuple(["user", "sponsors_listing"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsorship_for_viewer_as_sponsor(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    The sponsorship from the viewer to this user/organization; that is, the
    sponsorship where you're the sponsor. Only returns a sponsorship if it is
    active.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=user_login,
    ).sponsorship_for_viewer_as_sponsor()
    if not return_fields:
        op_stack = tuple(["user", "sponsorship_for_viewer_as_sponsor"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsorship_for_viewer_as_sponsorable(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    The sponsorship from this user/organization to the viewer; that is, the
    sponsorship you're receiving. Only returns a sponsorship if it is active.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=user_login,
    ).sponsorship_for_viewer_as_sponsorable()
    if not return_fields:
        op_stack = tuple(["user", "sponsorship_for_viewer_as_sponsorable"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsorship_newsletters(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    sponsorship_newsletters_after: str = None,
    sponsorship_newsletters_before: str = None,
    sponsorship_newsletters_first: int = None,
    sponsorship_newsletters_last: int = None,
    sponsorship_newsletters_order_by: graphql_schema.SponsorshipNewsletterOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    List of sponsorship updates sent from this sponsorable to sponsors.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        sponsorship_newsletters_after: Returns the elements in the list that
            come after the specified cursor.
        sponsorship_newsletters_before: Returns the elements in the list that
            come before the specified cursor.
        sponsorship_newsletters_first: Returns the first _n_ elements from the
            list.
        sponsorship_newsletters_last: Returns the last _n_ elements from the
            list.
        sponsorship_newsletters_order_by: Ordering options for sponsorship
            updates returned from the connection.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).sponsorship_newsletters(
        after=sponsorship_newsletters_after,
        before=sponsorship_newsletters_before,
        first=sponsorship_newsletters_first,
        last=sponsorship_newsletters_last,
        order_by=sponsorship_newsletters_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "sponsorship_newsletters"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsorships_as_maintainer(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    sponsorships_as_maintainer_after: str = None,
    sponsorships_as_maintainer_before: str = None,
    sponsorships_as_maintainer_first: int = None,
    sponsorships_as_maintainer_last: int = None,
    sponsorships_as_maintainer_include_private: bool = False,
    sponsorships_as_maintainer_order_by: graphql_schema.SponsorshipOrder = None,
) -> Dict[str, Any]:
    """
    This object's sponsorships as the maintainer.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        sponsorships_as_maintainer_after: Returns the elements in the list
            that come after the specified cursor.
        sponsorships_as_maintainer_before: Returns the elements in the list
            that come before the specified cursor.
        sponsorships_as_maintainer_first: Returns the first _n_ elements from
            the list.
        sponsorships_as_maintainer_last: Returns the last _n_ elements from
            the list.
        sponsorships_as_maintainer_include_private: Whether or not to include
            private sponsorships in the result set
        sponsorships_as_maintainer_order_by: Ordering options for sponsorships
            returned from this connection. If left blank, the
            sponsorships will be ordered based on relevancy to the
            viewer.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).sponsorships_as_maintainer(
        after=sponsorships_as_maintainer_after,
        before=sponsorships_as_maintainer_before,
        first=sponsorships_as_maintainer_first,
        last=sponsorships_as_maintainer_last,
        include_private=sponsorships_as_maintainer_include_private,
        order_by=sponsorships_as_maintainer_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "sponsorships_as_maintainer"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_sponsorships_as_sponsor(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    sponsorships_as_sponsor_after: str = None,
    sponsorships_as_sponsor_before: str = None,
    sponsorships_as_sponsor_first: int = None,
    sponsorships_as_sponsor_last: int = None,
    sponsorships_as_sponsor_order_by: graphql_schema.SponsorshipOrder = None,
) -> Dict[str, Any]:
    """
    This object's sponsorships as the sponsor.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        sponsorships_as_sponsor_after: Returns the elements in the list that
            come after the specified cursor.
        sponsorships_as_sponsor_before: Returns the elements in the list that
            come before the specified cursor.
        sponsorships_as_sponsor_first: Returns the first _n_ elements from the
            list.
        sponsorships_as_sponsor_last: Returns the last _n_ elements from the
            list.
        sponsorships_as_sponsor_order_by: Ordering options for sponsorships
            returned from this connection. If left blank, the
            sponsorships will be ordered based on relevancy to the
            viewer.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).sponsorships_as_sponsor(
        after=sponsorships_as_sponsor_after,
        before=sponsorships_as_sponsor_before,
        first=sponsorships_as_sponsor_first,
        last=sponsorships_as_sponsor_last,
        order_by=sponsorships_as_sponsor_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "sponsorships_as_sponsor"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_commit_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    commit_comments_after: str = None,
    commit_comments_before: str = None,
    commit_comments_first: int = None,
    commit_comments_last: int = None,
) -> Dict[str, Any]:
    """
    A list of commit comments made by this user.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
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
    op_settings = op.user(login=user_login,).commit_comments(
        after=commit_comments_after,
        before=commit_comments_before,
        first=commit_comments_first,
        last=commit_comments_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "commit_comments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_contributions_collection(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    contributions_collection_organization_id: str = None,
    contributions_collection_from_: datetime = None,
    contributions_collection_to: datetime = None,
) -> Dict[str, Any]:
    """
    The collection of contributions this user has made to different repositories.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        contributions_collection_organization_id: The ID of the organization
            used to filter contributions.
        contributions_collection_from_: Only contributions made at this time
            or later will be counted. If omitted, defaults to a year
            ago.
        contributions_collection_to: Only contributions made before and up to
            (including) this time will be counted. If omitted,
            defaults to the current time or one year from the provided
            from argument.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).contributions_collection(
        organization_id=contributions_collection_organization_id,
        from_=contributions_collection_from_,
        to=contributions_collection_to,
    )
    if not return_fields:
        op_stack = tuple(["user", "contributions_collection"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_followers(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    followers_after: str = None,
    followers_before: str = None,
    followers_first: int = None,
    followers_last: int = None,
) -> Dict[str, Any]:
    """
    A list of users the given user is followed by.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        followers_after: Returns the elements in the list that come after the
            specified cursor.
        followers_before: Returns the elements in the list that come before
            the specified cursor.
        followers_first: Returns the first _n_ elements from the list.
        followers_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).followers(
        after=followers_after,
        before=followers_before,
        first=followers_first,
        last=followers_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "followers"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_following(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    following_after: str = None,
    following_before: str = None,
    following_first: int = None,
    following_last: int = None,
) -> Dict[str, Any]:
    """
    A list of users the given user is following.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        following_after: Returns the elements in the list that come after the
            specified cursor.
        following_before: Returns the elements in the list that come before
            the specified cursor.
        following_first: Returns the first _n_ elements from the list.
        following_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).following(
        after=following_after,
        before=following_before,
        first=following_first,
        last=following_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "following"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_gist(
    user_login: str,
    gist_name: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    Find gist by repo name.

    Args:
        user_login: The user's login.
        gist_name: The gist name to find.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).gist(
        name=gist_name,
    )
    if not return_fields:
        op_stack = tuple(["user", "gist"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_gist_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    gist_comments_after: str = None,
    gist_comments_before: str = None,
    gist_comments_first: int = None,
    gist_comments_last: int = None,
) -> Dict[str, Any]:
    """
    A list of gist comments made by this user.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        gist_comments_after: Returns the elements in the list that come after
            the specified cursor.
        gist_comments_before: Returns the elements in the list that come
            before the specified cursor.
        gist_comments_first: Returns the first _n_ elements from the list.
        gist_comments_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).gist_comments(
        after=gist_comments_after,
        before=gist_comments_before,
        first=gist_comments_first,
        last=gist_comments_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "gist_comments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_gists(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    gists_privacy: graphql_schema.GistPrivacy = None,
    gists_order_by: graphql_schema.GistOrder = None,
    gists_after: str = None,
    gists_before: str = None,
    gists_first: int = None,
    gists_last: int = None,
) -> Dict[str, Any]:
    """
    A list of the Gists the user has created.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        gists_privacy: Filters Gists according to privacy.
        gists_order_by: Ordering options for gists returned from the
            connection
        gists_after: Returns the elements in the list that come after the
            specified cursor.
        gists_before: Returns the elements in the list that come before the
            specified cursor.
        gists_first: Returns the first _n_ elements from the list.
        gists_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).gists(
        privacy=gists_privacy,
        order_by=gists_order_by,
        after=gists_after,
        before=gists_before,
        first=gists_first,
        last=gists_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "gists"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_interaction_ability(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    The interaction ability settings for this user.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=user_login,
    ).interaction_ability()
    if not return_fields:
        op_stack = tuple(["user", "interaction_ability"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_issue_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    issue_comments_order_by: graphql_schema.IssueCommentOrder = None,
    issue_comments_after: str = None,
    issue_comments_before: str = None,
    issue_comments_first: int = None,
    issue_comments_last: int = None,
) -> Dict[str, Any]:
    """
    A list of issue comments made by this user.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        issue_comments_order_by: Ordering options for issue comments returned
            from the connection.
        issue_comments_after: Returns the elements in the list that come after
            the specified cursor.
        issue_comments_before: Returns the elements in the list that come
            before the specified cursor.
        issue_comments_first: Returns the first _n_ elements from the list.
        issue_comments_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).issue_comments(
        order_by=issue_comments_order_by,
        after=issue_comments_after,
        before=issue_comments_before,
        first=issue_comments_first,
        last=issue_comments_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "issue_comments"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_issues(
    user_login: str,
    issues_labels: str,
    issues_states: List[graphql_schema.IssueState],
    github_credentials: GitHubCredentials,
    *return_fields: str,
    issues_order_by: graphql_schema.IssueOrder = None,
    issues_filter_by: graphql_schema.IssueFilters = None,
    issues_after: str = None,
    issues_before: str = None,
    issues_first: int = None,
    issues_last: int = None,
) -> Dict[str, Any]:
    """
    A list of issues associated with this user.

    Args:
        user_login: The user's login.
        issues_labels: A list of label names to filter the pull requests by.
        issues_states: A list of states to filter the issues by.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
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
    op_settings = op.user(login=user_login,).issues(
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
        op_stack = tuple(["user", "issues"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_organization(
    user_login: str,
    organization_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    Find an organization by its login that the user belongs to.

    Args:
        user_login: The user's login.
        organization_login: The login of the organization to find.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).organization(
        login=organization_login,
    )
    if not return_fields:
        op_stack = tuple(["user", "organization"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_organizations(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    organizations_after: str = None,
    organizations_before: str = None,
    organizations_first: int = None,
    organizations_last: int = None,
) -> Dict[str, Any]:
    """
    A list of organizations the user belongs to.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        organizations_after: Returns the elements in the list that come after
            the specified cursor.
        organizations_before: Returns the elements in the list that come
            before the specified cursor.
        organizations_first: Returns the first _n_ elements from the list.
        organizations_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).organizations(
        after=organizations_after,
        before=organizations_before,
        first=organizations_first,
        last=organizations_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "organizations"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_public_keys(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    public_keys_after: str = None,
    public_keys_before: str = None,
    public_keys_first: int = None,
    public_keys_last: int = None,
) -> Dict[str, Any]:
    """
    A list of public keys associated with this user.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        public_keys_after: Returns the elements in the list that come after
            the specified cursor.
        public_keys_before: Returns the elements in the list that come before
            the specified cursor.
        public_keys_first: Returns the first _n_ elements from the list.
        public_keys_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).public_keys(
        after=public_keys_after,
        before=public_keys_before,
        first=public_keys_first,
        last=public_keys_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "public_keys"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_pull_requests(
    user_login: str,
    pull_requests_states: List[graphql_schema.PullRequestState],
    pull_requests_labels: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    pull_requests_head_ref_name: str = None,
    pull_requests_base_ref_name: str = None,
    pull_requests_order_by: graphql_schema.IssueOrder = None,
    pull_requests_after: str = None,
    pull_requests_before: str = None,
    pull_requests_first: int = None,
    pull_requests_last: int = None,
) -> Dict[str, Any]:
    """
    A list of pull requests associated with this user.

    Args:
        user_login: The user's login.
        pull_requests_states: A list of states to filter the pull requests by.
        pull_requests_labels: A list of label names to filter the pull
            requests by.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
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
    op_settings = op.user(login=user_login,).pull_requests(
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
        op_stack = tuple(["user", "pull_requests"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_repositories_contributed_to(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    repositories_contributed_to_privacy: graphql_schema.RepositoryPrivacy = None,
    repositories_contributed_to_order_by: graphql_schema.RepositoryOrder = None,
    repositories_contributed_to_is_locked: bool = None,
    repositories_contributed_to_include_user_repositories: bool = None,
    repositories_contributed_to_contribution_types: List[
        graphql_schema.RepositoryContributionType
    ] = None,
    repositories_contributed_to_after: str = None,
    repositories_contributed_to_before: str = None,
    repositories_contributed_to_first: int = None,
    repositories_contributed_to_last: int = None,
) -> Dict[str, Any]:
    """
    A list of repositories that the user recently contributed to.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        repositories_contributed_to_privacy: If non-null, filters repositories
            according to privacy
        repositories_contributed_to_order_by: Ordering options for
            repositories returned from the connection
        repositories_contributed_to_is_locked: If non-null, filters
            repositories according to whether they have been locked
        repositories_contributed_to_include_user_repositories: If true,
            include user repositories
        repositories_contributed_to_contribution_types: If non-null, include
            only the specified types of contributions. The GitHub.com
            UI uses [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]
        repositories_contributed_to_after: Returns the elements in the list
            that come after the specified cursor.
        repositories_contributed_to_before: Returns the elements in the list
            that come before the specified cursor.
        repositories_contributed_to_first: Returns the first _n_ elements from
            the list.
        repositories_contributed_to_last: Returns the last _n_ elements from
            the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).repositories_contributed_to(
        privacy=repositories_contributed_to_privacy,
        order_by=repositories_contributed_to_order_by,
        is_locked=repositories_contributed_to_is_locked,
        include_user_repositories=repositories_contributed_to_include_user_repositories,
        contribution_types=repositories_contributed_to_contribution_types,
        after=repositories_contributed_to_after,
        before=repositories_contributed_to_before,
        first=repositories_contributed_to_first,
        last=repositories_contributed_to_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "repositories_contributed_to"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_saved_replies(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    saved_replies_after: str = None,
    saved_replies_before: str = None,
    saved_replies_first: int = None,
    saved_replies_last: int = None,
    saved_replies_order_by: graphql_schema.SavedReplyOrder = {
        "field": "UPDATED_AT",
        "direction": "DESC",
    },
) -> Dict[str, Any]:
    """
    Replies this user has saved.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        saved_replies_after: Returns the elements in the list that come after
            the specified cursor.
        saved_replies_before: Returns the elements in the list that come
            before the specified cursor.
        saved_replies_first: Returns the first _n_ elements from the list.
        saved_replies_last: Returns the last _n_ elements from the list.
        saved_replies_order_by: The field to order saved replies by.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).saved_replies(
        after=saved_replies_after,
        before=saved_replies_before,
        first=saved_replies_first,
        last=saved_replies_last,
        order_by=saved_replies_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "saved_replies"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_starred_repositories(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    starred_repositories_after: str = None,
    starred_repositories_before: str = None,
    starred_repositories_first: int = None,
    starred_repositories_last: int = None,
    starred_repositories_owned_by_viewer: bool = None,
    starred_repositories_order_by: graphql_schema.StarOrder = None,
) -> Dict[str, Any]:
    """
    Repositories the user has starred.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        starred_repositories_after: Returns the elements in the list that come
            after the specified cursor.
        starred_repositories_before: Returns the elements in the list that
            come before the specified cursor.
        starred_repositories_first: Returns the first _n_ elements from the
            list.
        starred_repositories_last: Returns the last _n_ elements from the
            list.
        starred_repositories_owned_by_viewer: Filters starred repositories to
            only return repositories owned by the viewer.
        starred_repositories_order_by: Order for connection

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).starred_repositories(
        after=starred_repositories_after,
        before=starred_repositories_before,
        first=starred_repositories_first,
        last=starred_repositories_last,
        owned_by_viewer=starred_repositories_owned_by_viewer,
        order_by=starred_repositories_order_by,
    )
    if not return_fields:
        op_stack = tuple(["user", "starred_repositories"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_status(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
) -> Dict[str, Any]:
    """
    The user's description of what they're currently doing.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        login=user_login,
    ).status()
    if not return_fields:
        op_stack = tuple(["user", "status"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_top_repositories(
    user_login: str,
    top_repositories_order_by: graphql_schema.RepositoryOrder,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    top_repositories_after: str = None,
    top_repositories_before: str = None,
    top_repositories_first: int = None,
    top_repositories_last: int = None,
    top_repositories_since: datetime = None,
) -> Dict[str, Any]:
    """
    Repositories the user has contributed to, ordered by contribution rank, plus
    repositories the user has created .

    Args:
        user_login: The user's login.
        top_repositories_order_by: Ordering options for repositories returned
            from the connection
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        top_repositories_after: Returns the elements in the list that come
            after the specified cursor.
        top_repositories_before: Returns the elements in the list that come
            before the specified cursor.
        top_repositories_first: Returns the first _n_ elements from the list.
        top_repositories_last: Returns the last _n_ elements from the list.
        top_repositories_since: How far back in time to fetch contributed
            repositories

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).top_repositories(
        order_by=top_repositories_order_by,
        after=top_repositories_after,
        before=top_repositories_before,
        first=top_repositories_first,
        last=top_repositories_last,
        since=top_repositories_since,
    )
    if not return_fields:
        op_stack = tuple(["user", "top_repositories"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result


@task()
def query_user_watching(
    user_login: str,
    github_credentials: GitHubCredentials,
    *return_fields: str,
    watching_privacy: graphql_schema.RepositoryPrivacy = None,
    watching_order_by: graphql_schema.RepositoryOrder = None,
    watching_affiliations: List[graphql_schema.RepositoryAffiliation] = None,
    watching_owner_affiliations: List[graphql_schema.RepositoryAffiliation] = [
        "OWNER",
        "COLLABORATOR",
    ],
    watching_is_locked: bool = None,
    watching_after: str = None,
    watching_before: str = None,
    watching_first: int = None,
    watching_last: int = None,
) -> Dict[str, Any]:
    """
    A list of repositories the given user is watching.

    Args:
        user_login: The user's login.
        github_credentials: github: Credentials to use for authentication with
            GitHub.
        *return_fields: return_fields: Subset the return fields; defaults to
            fields listed in configs/query/*.json.
        watching_privacy: If non-null, filters repositories according to
            privacy
        watching_order_by: Ordering options for repositories returned from the
            connection
        watching_affiliations: Affiliation options for repositories returned
            from the connection. If none specified, the results will
            include repositories for which the current viewer is an
            owner or collaborator, or member.
        watching_owner_affiliations: Array of owner's affiliation options for
            repositories returned from the connection. For example,
            OWNER will include only repositories that the organization
            or user being viewed owns.
        watching_is_locked: If non-null, filters repositories according to
            whether they have been locked
        watching_after: Returns the elements in the list that come after the
            specified cursor.
        watching_before: Returns the elements in the list that come before the
            specified cursor.
        watching_first: Returns the first _n_ elements from the list.
        watching_last: Returns the last _n_ elements from the list.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login,).watching(
        privacy=watching_privacy,
        order_by=watching_order_by,
        affiliations=watching_affiliations,
        owner_affiliations=watching_owner_affiliations,
        is_locked=watching_is_locked,
        after=watching_after,
        before=watching_before,
        first=watching_first,
        last=watching_last,
    )
    if not return_fields:
        op_stack = tuple(["user", "watching"])
        return_fields = return_fields_defaults[op_stack]
    op_settings.__fields__(*return_fields)

    result = _execute_graphql_op(op, github_credentials)
    return result
