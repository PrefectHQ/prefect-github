"""
This is a module for interacting with GitHub Query user tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials
from prefect_github.graphql import _execute_graphql_op
from prefect_github.schemas import graphql_schema
from prefect_github.utils import initialize_return_fields_defaults, strip_kwargs

config_path = Path(__file__).parent.resolve() / "configs" / "query" / "user.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task()
async def query_user(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The query root of GitHub's GraphQL interface.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    )

    if not return_fields:
        op_stack = ("user",)
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]


@task()
async def query_user_packages(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    names: Iterable[str] = None,
    repository_id: str = None,
    package_type: graphql_schema.PackageType = None,
    order_by: graphql_schema.PackageOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of packages under the owner.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        names: Find packages by their names.
        repository_id: Find packages in a repository by ID.
        package_type: Filter registry package by type.
        order_by: Ordering of the returned packages.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).packages(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            names=names,
            repository_id=repository_id,
            package_type=package_type,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "packages",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["packages"]


@task()
async def query_user_project(
    login: str,
    number: int,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Find project by number.

    Args:
        login: The user's login.
        number: The project number to find.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).project(
        **strip_kwargs(
            number=number,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "project",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["project"]


@task()
async def query_user_projects(
    login: str,
    states: Iterable[graphql_schema.ProjectState],
    github_credentials: GitHubCredentials,
    order_by: graphql_schema.ProjectOrder = None,
    search: str = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of projects under the owner.

    Args:
        login: The user's login.
        states: A list of states to filter the projects by.
        github_credentials: Credentials to use for authentication with GitHub.
        order_by: Ordering options for projects returned from the
            connection.
        search: Query to search projects by, currently only searching
            by name.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).projects(
        **strip_kwargs(
            states=states,
            order_by=order_by,
            search=search,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "projects",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["projects"]


@task()
async def query_user_project_next(
    login: str,
    number: int,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Find a project by project (beta) number.

    Args:
        login: The user's login.
        number: The project (beta) number.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).project_next(
        **strip_kwargs(
            number=number,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "projectNext",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["projectNext"]


@task()
async def query_user_projects_next(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    query: str = None,
    sort_by: graphql_schema.ProjectNextOrderField = "TITLE",
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of projects (beta) under the owner.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        query: A project (beta) to search for under the the owner.
        sort_by: How to order the returned projects (beta).
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).projects_next(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            query=query,
            sort_by=sort_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "projectsNext",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["projectsNext"]


@task()
async def query_user_repository_discussions(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    order_by: graphql_schema.DiscussionOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
    repository_id: str = None,
    answered: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Discussions this user has started.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come
            after the specified cursor.
        before: Returns the elements in the list that
            come before the specified cursor.
        first: Returns the first _n_ elements from the
            list.
        last: Returns the last _n_ elements from the
            list.
        order_by: Ordering options for discussions
            returned from the connection.
        repository_id: Filter discussions to only those
            in a specific repository.
        answered: Filter discussions to only those that
            have been answered or not. Defaults to including both
            answered and unanswered discussions.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).repository_discussions(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            order_by=order_by,
            repository_id=repository_id,
            answered=answered,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "repositoryDiscussions",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["repositoryDiscussions"]


@task()
async def query_user_repository_discussion_comments(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    repository_id: str = None,
    only_answers: bool = False,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Discussion comments this user has authored.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list
            that come after the specified cursor.
        before: Returns the elements in the list
            that come before the specified cursor.
        first: Returns the first _n_ elements
            from the list.
        last: Returns the last _n_ elements from
            the list.
        repository_id: Filter discussion comments
            to only those in a specific repository.
        only_answers: Filter discussion comments
            to only those that were marked as the answer.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).repository_discussion_comments(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            repository_id=repository_id,
            only_answers=only_answers,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "repositoryDiscussionComments",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["repositoryDiscussionComments"]


@task()
async def query_user_repositories(
    login: str,
    github_credentials: GitHubCredentials,
    privacy: graphql_schema.RepositoryPrivacy = None,
    order_by: graphql_schema.RepositoryOrder = None,
    affiliations: Iterable[graphql_schema.RepositoryAffiliation] = None,
    owner_affiliations: Iterable[graphql_schema.RepositoryAffiliation] = [
        "OWNER",
        "COLLABORATOR",
    ],
    is_locked: bool = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    is_fork: bool = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of repositories that the user owns.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        privacy: If non-null, filters repositories according to
            privacy.
        order_by: Ordering options for repositories returned from
            the connection.
        affiliations: Array of viewer's affiliation options for
            repositories returned from the connection. For example,
            OWNER will include only repositories that the current viewer
            owns.
        owner_affiliations: Array of owner's affiliation options
            for repositories returned from the connection. For example,
            OWNER will include only repositories that the organization
            or user being viewed owns.
        is_locked: If non-null, filters repositories according to
            whether they have been locked.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        is_fork: If non-null, filters repositories according to
            whether they are forks of another repository.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).repositories(
        **strip_kwargs(
            privacy=privacy,
            order_by=order_by,
            affiliations=affiliations,
            owner_affiliations=owner_affiliations,
            is_locked=is_locked,
            after=after,
            before=before,
            first=first,
            last=last,
            is_fork=is_fork,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "repositories",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["repositories"]


@task()
async def query_user_repository(
    login: str,
    name: str,
    github_credentials: GitHubCredentials,
    follow_renames: bool = True,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Find Repository.

    Args:
        login: The user's login.
        name: Name of Repository to find.
        github_credentials: Credentials to use for authentication with GitHub.
        follow_renames: Follow repository renames. If disabled, a
            repository referenced by its old name will return an error.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).repository(
        **strip_kwargs(
            name=name,
            follow_renames=follow_renames,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "repository",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["repository"]


@task()
async def query_user_item_showcase(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Showcases a selection of repositories and gists that the profile owner has
    either curated or that have been selected automatically based on popularity.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    ).item_showcase(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "user",
            "itemShowcase",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["itemShowcase"]


@task()
async def query_user_pinnable_items(
    login: str,
    types: Iterable[graphql_schema.PinnableItemType],
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of repositories and gists this profile owner can pin to their profile.

    Args:
        login: The user's login.
        types: Filter the types of pinnable items that are
            returned.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).pinnable_items(
        **strip_kwargs(
            types=types,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "pinnableItems",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["pinnableItems"]


@task()
async def query_user_pinned_items(
    login: str,
    types: Iterable[graphql_schema.PinnableItemType],
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of repositories and gists this profile owner has pinned to their profile.

    Args:
        login: The user's login.
        types: Filter the types of pinned items that are returned.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).pinned_items(
        **strip_kwargs(
            types=types,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "pinnedItems",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["pinnedItems"]


@task()
async def query_user_sponsoring(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    order_by: graphql_schema.SponsorOrder = {"field": "RELEVANCE", "direction": "DESC"},
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    List of users and organizations this entity is sponsoring.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        order_by: Ordering options for the users and organizations
            returned from the connection.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).sponsoring(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "sponsoring",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsoring"]


@task()
async def query_user_sponsors(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    tier_id: str = None,
    order_by: graphql_schema.SponsorOrder = {"field": "RELEVANCE", "direction": "DESC"},
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    List of sponsors for this user or organization.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        tier_id: If given, will filter for sponsors at the given tier.
            Will only return sponsors whose tier the viewer is permitted
            to see.
        order_by: Ordering options for sponsors returned from the
            connection.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).sponsors(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            tier_id=tier_id,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "sponsors",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsors"]


@task()
async def query_user_sponsors_activities(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    period: graphql_schema.SponsorsActivityPeriod = "MONTH",
    order_by: graphql_schema.SponsorsActivityOrder = {
        "field": "TIMESTAMP",
        "direction": "DESC",
    },
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Events involving this sponsorable, such as new sponsorships.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come
            after the specified cursor.
        before: Returns the elements in the list that come
            before the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        period: Filter activities returned to only those
            that occurred in a given time range.
        order_by: Ordering options for activity returned
            from the connection.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).sponsors_activities(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            period=period,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "sponsorsActivities",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorsActivities"]


@task()
async def query_user_sponsors_listing(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The GitHub Sponsors listing for this user or organization.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    ).sponsors_listing(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "user",
            "sponsorsListing",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorsListing"]


@task()
async def query_user_sponsorship_for_viewer_as_sponsor(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The sponsorship from the viewer to this user/organization; that is, the
    sponsorship where you're the sponsor. Only returns a sponsorship if it is
    active.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    ).sponsorship_for_viewer_as_sponsor(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "user",
            "sponsorshipForViewerAsSponsor",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorshipForViewerAsSponsor"]


@task()
async def query_user_sponsorship_for_viewer_as_sponsorable(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The sponsorship from this user/organization to the viewer; that is, the
    sponsorship you're receiving. Only returns a sponsorship if it is active.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    ).sponsorship_for_viewer_as_sponsorable(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "user",
            "sponsorshipForViewerAsSponsorable",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorshipForViewerAsSponsorable"]


@task()
async def query_user_sponsorship_newsletters(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    order_by: graphql_schema.SponsorshipNewsletterOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    List of sponsorship updates sent from this sponsorable to sponsors.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that
            come after the specified cursor.
        before: Returns the elements in the list that
            come before the specified cursor.
        first: Returns the first _n_ elements from the
            list.
        last: Returns the last _n_ elements from the
            list.
        order_by: Ordering options for sponsorship
            updates returned from the connection.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).sponsorship_newsletters(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "sponsorshipNewsletters",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorshipNewsletters"]


@task()
async def query_user_sponsorships_as_maintainer(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    include_private: bool = False,
    order_by: graphql_schema.SponsorshipOrder = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    This object's sponsorships as the maintainer.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that
            come after the specified cursor.
        before: Returns the elements in the list that
            come before the specified cursor.
        first: Returns the first _n_ elements from
            the list.
        last: Returns the last _n_ elements from the
            list.
        include_private: Whether or not to include
            private sponsorships in the result set.
        order_by: Ordering options for sponsorships
            returned from this connection. If left blank, the
            sponsorships will be ordered based on relevancy to the
            viewer.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).sponsorships_as_maintainer(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            include_private=include_private,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "sponsorshipsAsMaintainer",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorshipsAsMaintainer"]


@task()
async def query_user_sponsorships_as_sponsor(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    order_by: graphql_schema.SponsorshipOrder = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    This object's sponsorships as the sponsor.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that
            come after the specified cursor.
        before: Returns the elements in the list that
            come before the specified cursor.
        first: Returns the first _n_ elements from the
            list.
        last: Returns the last _n_ elements from the
            list.
        order_by: Ordering options for sponsorships
            returned from this connection. If left blank, the
            sponsorships will be ordered based on relevancy to the
            viewer.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).sponsorships_as_sponsor(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "sponsorshipsAsSponsor",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["sponsorshipsAsSponsor"]


@task()
async def query_user_commit_comments(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of commit comments made by this user.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come
            before the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).commit_comments(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "commitComments",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["commitComments"]


@task()
async def query_user_contributions_collection(
    login: str,
    github_credentials: GitHubCredentials,
    organization_id: str = None,
    from_: datetime = None,
    to: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The collection of contributions this user has made to different repositories.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        organization_id: The ID of the organization
            used to filter contributions.
        from_: Only contributions made at this time or
            later will be counted. If omitted, defaults to a year ago.
        to: Only contributions made before and up to
            (including) this time will be counted. If omitted, defaults
            to the current time or one year from the provided from
            argument.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).contributions_collection(
        **strip_kwargs(
            organization_id=organization_id,
            from_=from_,
            to=to,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "contributionsCollection",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["contributionsCollection"]


@task()
async def query_user_followers(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of users the given user is followed by.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).followers(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "followers",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["followers"]


@task()
async def query_user_following(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of users the given user is following.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).following(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "following",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["following"]


@task()
async def query_user_gist(
    login: str,
    name: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Find gist by repo name.

    Args:
        login: The user's login.
        name: The gist name to find.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).gist(
        **strip_kwargs(
            name=name,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "gist",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["gist"]


@task()
async def query_user_gist_comments(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of gist comments made by this user.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).gist_comments(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "gistComments",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["gistComments"]


@task()
async def query_user_gists(
    login: str,
    github_credentials: GitHubCredentials,
    privacy: graphql_schema.GistPrivacy = None,
    order_by: graphql_schema.GistOrder = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of the Gists the user has created.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        privacy: Filters Gists according to privacy.
        order_by: Ordering options for gists returned from the connection.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).gists(
        **strip_kwargs(
            privacy=privacy,
            order_by=order_by,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "gists",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["gists"]


@task()
async def query_user_interaction_ability(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The interaction ability settings for this user.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    ).interaction_ability(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "user",
            "interactionAbility",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["interactionAbility"]


@task()
async def query_user_issue_comments(
    login: str,
    github_credentials: GitHubCredentials,
    order_by: graphql_schema.IssueCommentOrder = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of issue comments made by this user.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        order_by: Ordering options for issue comments returned
            from the connection.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).issue_comments(
        **strip_kwargs(
            order_by=order_by,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "issueComments",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["issueComments"]


@task()
async def query_user_issues(
    login: str,
    labels: Iterable[str],
    states: Iterable[graphql_schema.IssueState],
    github_credentials: GitHubCredentials,
    order_by: graphql_schema.IssueOrder = None,
    filter_by: graphql_schema.IssueFilters = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of issues associated with this user.

    Args:
        login: The user's login.
        labels: A list of label names to filter the pull requests by.
        states: A list of states to filter the issues by.
        github_credentials: Credentials to use for authentication with GitHub.
        order_by: Ordering options for issues returned from the
            connection.
        filter_by: Filtering options for issues returned from the
            connection.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).issues(
        **strip_kwargs(
            labels=labels,
            states=states,
            order_by=order_by,
            filter_by=filter_by,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "issues",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["issues"]


@task()
async def query_user_organization(
    login: str,
    organization_login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Find an organization by its login that the user belongs to.

    Args:
        login: The user's login.
        organization_login: The login of the organization to find.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).organization(
        **strip_kwargs(
            login=organization_login,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "organization",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["organization"]


@task()
async def query_user_organizations(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of organizations the user belongs to.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).organizations(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "organizations",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["organizations"]


@task()
async def query_user_public_keys(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of public keys associated with this user.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).public_keys(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "publicKeys",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["publicKeys"]


@task()
async def query_user_pull_requests(
    login: str,
    states: Iterable[graphql_schema.PullRequestState],
    labels: Iterable[str],
    github_credentials: GitHubCredentials,
    head_ref_name: str = None,
    base_ref_name: str = None,
    order_by: graphql_schema.IssueOrder = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of pull requests associated with this user.

    Args:
        login: The user's login.
        states: A list of states to filter the pull requests by.
        labels: A list of label names to filter the pull requests
            by.
        github_credentials: Credentials to use for authentication with GitHub.
        head_ref_name: The head ref name to filter the pull
            requests by.
        base_ref_name: The base ref name to filter the pull
            requests by.
        order_by: Ordering options for pull requests returned from
            the connection.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).pull_requests(
        **strip_kwargs(
            states=states,
            labels=labels,
            head_ref_name=head_ref_name,
            base_ref_name=base_ref_name,
            order_by=order_by,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "pullRequests",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["pullRequests"]


@task()
async def query_user_repositories_contributed_to(
    login: str,
    github_credentials: GitHubCredentials,
    privacy: graphql_schema.RepositoryPrivacy = None,
    order_by: graphql_schema.RepositoryOrder = None,
    is_locked: bool = None,
    include_user_repositories: bool = None,
    contribution_types: Iterable[graphql_schema.RepositoryContributionType] = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of repositories that the user recently contributed to.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        privacy: If non-null, filters repositories
            according to privacy.
        order_by: Ordering options for repositories
            returned from the connection.
        is_locked: If non-null, filters repositories
            according to whether they have been locked.
        include_user_repositories: If true, include
            user repositories.
        contribution_types: If non-null, include
            only the specified types of contributions. The GitHub.com UI
            uses [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY].
        after: Returns the elements in the list that
            come after the specified cursor.
        before: Returns the elements in the list
            that come before the specified cursor.
        first: Returns the first _n_ elements from
            the list.
        last: Returns the last _n_ elements from the
            list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).repositories_contributed_to(
        **strip_kwargs(
            privacy=privacy,
            order_by=order_by,
            is_locked=is_locked,
            include_user_repositories=include_user_repositories,
            contribution_types=contribution_types,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "repositoriesContributedTo",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["repositoriesContributedTo"]


@task()
async def query_user_saved_replies(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    order_by: graphql_schema.SavedReplyOrder = {
        "field": "UPDATED_AT",
        "direction": "DESC",
    },
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Replies this user has saved.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come before
            the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        order_by: The field to order saved replies by.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).saved_replies(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "savedReplies",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["savedReplies"]


@task()
async def query_user_starred_repositories(
    login: str,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    owned_by_viewer: bool = None,
    order_by: graphql_schema.StarOrder = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Repositories the user has starred.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come
            after the specified cursor.
        before: Returns the elements in the list that come
            before the specified cursor.
        first: Returns the first _n_ elements from the
            list.
        last: Returns the last _n_ elements from the list.
        owned_by_viewer: Filters starred repositories to
            only return repositories owned by the viewer.
        order_by: Order for connection.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).starred_repositories(
        **strip_kwargs(
            after=after,
            before=before,
            first=first,
            last=last,
            owned_by_viewer=owned_by_viewer,
            order_by=order_by,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "starredRepositories",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["starredRepositories"]


@task()
async def query_user_status(
    login: str,
    github_credentials: GitHubCredentials,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    The user's description of what they're currently doing.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(
        **strip_kwargs(
            login=login,
        )
    ).status(**strip_kwargs())

    if not return_fields:
        op_stack = (
            "user",
            "status",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["status"]


@task()
async def query_user_top_repositories(
    login: str,
    order_by: graphql_schema.RepositoryOrder,
    github_credentials: GitHubCredentials,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    since: datetime = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    Repositories the user has contributed to, ordered by contribution rank, plus
    repositories the user has created.

    Args:
        login: The user's login.
        order_by: Ordering options for repositories returned
            from the connection.
        github_credentials: Credentials to use for authentication with GitHub.
        after: Returns the elements in the list that come after
            the specified cursor.
        before: Returns the elements in the list that come
            before the specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        since: How far back in time to fetch contributed
            repositories.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).top_repositories(
        **strip_kwargs(
            order_by=order_by,
            after=after,
            before=before,
            first=first,
            last=last,
            since=since,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "topRepositories",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["topRepositories"]


@task()
async def query_user_watching(
    login: str,
    github_credentials: GitHubCredentials,
    privacy: graphql_schema.RepositoryPrivacy = None,
    order_by: graphql_schema.RepositoryOrder = None,
    affiliations: Iterable[graphql_schema.RepositoryAffiliation] = None,
    owner_affiliations: Iterable[graphql_schema.RepositoryAffiliation] = [
        "OWNER",
        "COLLABORATOR",
    ],
    is_locked: bool = None,
    after: str = None,
    before: str = None,
    first: int = None,
    last: int = None,
    return_fields: Iterable[str] = None,
) -> Dict[str, Any]:
    """
    A list of repositories the given user is watching.

    Args:
        login: The user's login.
        github_credentials: Credentials to use for authentication with GitHub.
        privacy: If non-null, filters repositories according to privacy.
        order_by: Ordering options for repositories returned from the
            connection.
        affiliations: Affiliation options for repositories returned
            from the connection. If none specified, the results will
            include repositories for which the current viewer is an
            owner or collaborator, or member.
        owner_affiliations: Array of owner's affiliation options for
            repositories returned from the connection. For example,
            OWNER will include only repositories that the organization
            or user being viewed owns.
        is_locked: If non-null, filters repositories according to
            whether they have been locked.
        after: Returns the elements in the list that come after the
            specified cursor.
        before: Returns the elements in the list that come before the
            specified cursor.
        first: Returns the first _n_ elements from the list.
        last: Returns the last _n_ elements from the list.
        return_fields: Subset the return fields (as snake_case); defaults to
            fields listed in configs/query/*.json.

    Returns:
        A dict of the returned fields.
    """
    op = Operation(graphql_schema.Query)
    op_settings = op.user(**strip_kwargs(login=login,)).watching(
        **strip_kwargs(
            privacy=privacy,
            order_by=order_by,
            affiliations=affiliations,
            owner_affiliations=owner_affiliations,
            is_locked=is_locked,
            after=after,
            before=before,
            first=first,
            last=last,
        )
    )

    if not return_fields:
        op_stack = (
            "user",
            "watching",
        )
        return_fields = return_fields_defaults[op_stack]
    elif isinstance(return_fields, str):
        return_fields = (return_fields,)

    try:
        op_settings.__fields__(*return_fields)
    except KeyError:  # nested under node
        op_settings.nodes().__fields__(*return_fields)

    result = await _execute_graphql_op(op, github_credentials)
    return result["user"]["watching"]
