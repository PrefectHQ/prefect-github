"""This is a module for interacting with GitHub user tasks"""

from datetime import datetime
from pathlib import Path
from typing import List

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials
from prefect_github.schemas import graphql_schema
from prefect_github.utils import initialize_return_fields_defaults

config_path = Path("configs") / "query" / "user.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
def query_user(
    login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=login)

    if not return_fields:
        op_stack = ("user",)
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]


@task
def query_user_packages(
    user_login: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).packages(
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
        op_stack = ("user", "packages")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["packages"]


@task
def query_user_project(
    user_login: str,
    project_number: int,
    github_credentials: GitHubCredentials,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).project(number=project_number)

    if not return_fields:
        op_stack = ("user", "project")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["project"]


@task
def query_user_projects(
    user_login: str,
    projects_states: List[graphql_schema.ProjectState],
    github_credentials: GitHubCredentials,
    projects_order_by: graphql_schema.ProjectOrder = None,
    projects_search: str = None,
    projects_after: str = None,
    projects_before: str = None,
    projects_first: int = None,
    projects_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).projects(
        order_by=projects_order_by,
        search=projects_search,
        states=projects_states,
        after=projects_after,
        before=projects_before,
        first=projects_first,
        last=projects_last,
    )

    if not return_fields:
        op_stack = ("user", "projects")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["projects"]


@task
def query_user_project_next(
    user_login: str,
    project_next_number: int,
    github_credentials: GitHubCredentials,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).project_next(number=project_next_number)

    if not return_fields:
        op_stack = ("user", "projectNext")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["project_next"]


@task
def query_user_projects_next(
    user_login: str,
    github_credentials: GitHubCredentials,
    projects_next_after: str = None,
    projects_next_before: str = None,
    projects_next_first: int = None,
    projects_next_last: int = None,
    projects_next_query: str = None,
    projects_next_sort_by: graphql_schema.ProjectNextOrderField = "TITLE",
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).projects_next(
        after=projects_next_after,
        before=projects_next_before,
        first=projects_next_first,
        last=projects_next_last,
        query=projects_next_query,
        sort_by=projects_next_sort_by,
    )

    if not return_fields:
        op_stack = ("user", "projectsNext")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["projects_next"]


@task
def query_user_repository_discussions(
    user_login: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).repository_discussions(
        after=repository_discussions_after,
        before=repository_discussions_before,
        first=repository_discussions_first,
        last=repository_discussions_last,
        order_by=repository_discussions_order_by,
        repository_id=repository_discussions_repository_id,
        answered=repository_discussions_answered,
    )

    if not return_fields:
        op_stack = ("user", "repositoryDiscussions")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["repository_discussions"]


@task
def query_user_repository_discussion_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    repository_discussion_comments_after: str = None,
    repository_discussion_comments_before: str = None,
    repository_discussion_comments_first: int = None,
    repository_discussion_comments_last: int = None,
    repository_discussion_comments_repository_id: str = None,
    repository_discussion_comments_only_answers: bool = False,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).repository_discussion_comments(
        after=repository_discussion_comments_after,
        before=repository_discussion_comments_before,
        first=repository_discussion_comments_first,
        last=repository_discussion_comments_last,
        repository_id=repository_discussion_comments_repository_id,
        only_answers=repository_discussion_comments_only_answers,
    )

    if not return_fields:
        op_stack = ("user", "repositoryDiscussionComments")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["repository_discussion_comments"]


@task
def query_user_repositories(
    user_login: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).repositories(
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
        op_stack = ("user", "repositories")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["repositories"]


@task
def query_user_repository(
    user_login: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).repository(
        name=repository_name, follow_renames=repository_follow_renames
    )

    if not return_fields:
        op_stack = ("user", "repository")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["repository"]


@task
def query_user_item_showcase(
    user_login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login)

    if not return_fields:
        op_stack = ("user", "itemShowcase")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["item_showcase"]


@task
def query_user_pinnable_items(
    user_login: str,
    pinnable_items_types: List[graphql_schema.PinnableItemType],
    github_credentials: GitHubCredentials,
    pinnable_items_after: str = None,
    pinnable_items_before: str = None,
    pinnable_items_first: int = None,
    pinnable_items_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).pinnable_items(
        types=pinnable_items_types,
        after=pinnable_items_after,
        before=pinnable_items_before,
        first=pinnable_items_first,
        last=pinnable_items_last,
    )

    if not return_fields:
        op_stack = ("user", "pinnableItems")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["pinnable_items"]


@task
def query_user_pinned_items(
    user_login: str,
    pinned_items_types: List[graphql_schema.PinnableItemType],
    github_credentials: GitHubCredentials,
    pinned_items_after: str = None,
    pinned_items_before: str = None,
    pinned_items_first: int = None,
    pinned_items_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).pinned_items(
        types=pinned_items_types,
        after=pinned_items_after,
        before=pinned_items_before,
        first=pinned_items_first,
        last=pinned_items_last,
    )

    if not return_fields:
        op_stack = ("user", "pinnedItems")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["pinned_items"]


@task
def query_user_sponsoring(
    user_login: str,
    github_credentials: GitHubCredentials,
    sponsoring_after: str = None,
    sponsoring_before: str = None,
    sponsoring_first: int = None,
    sponsoring_last: int = None,
    sponsoring_order_by: graphql_schema.SponsorOrder = {
        "field": "RELEVANCE",
        "direction": "DESC",
    },
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).sponsoring(
        after=sponsoring_after,
        before=sponsoring_before,
        first=sponsoring_first,
        last=sponsoring_last,
        order_by=sponsoring_order_by,
    )

    if not return_fields:
        op_stack = ("user", "sponsoring")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsoring"]


@task
def query_user_sponsors(
    user_login: str,
    github_credentials: GitHubCredentials,
    sponsors_after: str = None,
    sponsors_before: str = None,
    sponsors_first: int = None,
    sponsors_last: int = None,
    sponsors_tier_id: str = None,
    sponsors_order_by: graphql_schema.SponsorOrder = {
        "field": "RELEVANCE",
        "direction": "DESC",
    },
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).sponsors(
        after=sponsors_after,
        before=sponsors_before,
        first=sponsors_first,
        last=sponsors_last,
        tier_id=sponsors_tier_id,
        order_by=sponsors_order_by,
    )

    if not return_fields:
        op_stack = ("user", "sponsors")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsors"]


@task
def query_user_sponsors_activities(
    user_login: str,
    github_credentials: GitHubCredentials,
    sponsors_activities_after: str = None,
    sponsors_activities_before: str = None,
    sponsors_activities_first: int = None,
    sponsors_activities_last: int = None,
    sponsors_activities_period: graphql_schema.SponsorsActivityPeriod = "MONTH",
    sponsors_activities_order_by: graphql_schema.SponsorsActivityOrder = {
        "field": "TIMESTAMP",
        "direction": "DESC",
    },
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).sponsors_activities(
        after=sponsors_activities_after,
        before=sponsors_activities_before,
        first=sponsors_activities_first,
        last=sponsors_activities_last,
        period=sponsors_activities_period,
        order_by=sponsors_activities_order_by,
    )

    if not return_fields:
        op_stack = ("user", "sponsorsActivities")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsors_activities"]


@task
def query_user_sponsors_listing(
    user_login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login)

    if not return_fields:
        op_stack = ("user", "sponsorsListing")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsors_listing"]


@task
def query_user_sponsorship_for_viewer_as_sponsor(
    user_login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login)

    if not return_fields:
        op_stack = ("user", "sponsorshipForViewerAsSponsor")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsorship_for_viewer_as_sponsor"]


@task
def query_user_sponsorship_for_viewer_as_sponsorable(
    user_login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login)

    if not return_fields:
        op_stack = ("user", "sponsorshipForViewerAsSponsorable")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsorship_for_viewer_as_sponsorable"]


@task
def query_user_sponsorship_newsletters(
    user_login: str,
    github_credentials: GitHubCredentials,
    sponsorship_newsletters_after: str = None,
    sponsorship_newsletters_before: str = None,
    sponsorship_newsletters_first: int = None,
    sponsorship_newsletters_last: int = None,
    sponsorship_newsletters_order_by: graphql_schema.SponsorshipNewsletterOrder = {
        "field": "CREATED_AT",
        "direction": "DESC",
    },
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).sponsorship_newsletters(
        after=sponsorship_newsletters_after,
        before=sponsorship_newsletters_before,
        first=sponsorship_newsletters_first,
        last=sponsorship_newsletters_last,
        order_by=sponsorship_newsletters_order_by,
    )

    if not return_fields:
        op_stack = ("user", "sponsorshipNewsletters")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsorship_newsletters"]


@task
def query_user_sponsorships_as_maintainer(
    user_login: str,
    github_credentials: GitHubCredentials,
    sponsorships_as_maintainer_after: str = None,
    sponsorships_as_maintainer_before: str = None,
    sponsorships_as_maintainer_first: int = None,
    sponsorships_as_maintainer_last: int = None,
    sponsorships_as_maintainer_include_private: bool = False,
    sponsorships_as_maintainer_order_by: graphql_schema.SponsorshipOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).sponsorships_as_maintainer(
        after=sponsorships_as_maintainer_after,
        before=sponsorships_as_maintainer_before,
        first=sponsorships_as_maintainer_first,
        last=sponsorships_as_maintainer_last,
        include_private=sponsorships_as_maintainer_include_private,
        order_by=sponsorships_as_maintainer_order_by,
    )

    if not return_fields:
        op_stack = ("user", "sponsorshipsAsMaintainer")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsorships_as_maintainer"]


@task
def query_user_sponsorships_as_sponsor(
    user_login: str,
    github_credentials: GitHubCredentials,
    sponsorships_as_sponsor_after: str = None,
    sponsorships_as_sponsor_before: str = None,
    sponsorships_as_sponsor_first: int = None,
    sponsorships_as_sponsor_last: int = None,
    sponsorships_as_sponsor_order_by: graphql_schema.SponsorshipOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).sponsorships_as_sponsor(
        after=sponsorships_as_sponsor_after,
        before=sponsorships_as_sponsor_before,
        first=sponsorships_as_sponsor_first,
        last=sponsorships_as_sponsor_last,
        order_by=sponsorships_as_sponsor_order_by,
    )

    if not return_fields:
        op_stack = ("user", "sponsorshipsAsSponsor")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["sponsorships_as_sponsor"]


@task
def query_user_commit_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    commit_comments_after: str = None,
    commit_comments_before: str = None,
    commit_comments_first: int = None,
    commit_comments_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).commit_comments(
        after=commit_comments_after,
        before=commit_comments_before,
        first=commit_comments_first,
        last=commit_comments_last,
    )

    if not return_fields:
        op_stack = ("user", "commitComments")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["commit_comments"]


@task
def query_user_contributions_collection(
    user_login: str,
    github_credentials: GitHubCredentials,
    contributions_collection_organization_id: str = None,
    contributions_collection_from_: datetime = None,
    contributions_collection_to: datetime = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).contributions_collection(
        organization_id=contributions_collection_organization_id,
        from_=contributions_collection_from_,
        to=contributions_collection_to,
    )

    if not return_fields:
        op_stack = ("user", "contributionsCollection")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["contributions_collection"]


@task
def query_user_followers(
    user_login: str,
    github_credentials: GitHubCredentials,
    followers_after: str = None,
    followers_before: str = None,
    followers_first: int = None,
    followers_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).followers(
        after=followers_after,
        before=followers_before,
        first=followers_first,
        last=followers_last,
    )

    if not return_fields:
        op_stack = ("user", "followers")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["followers"]


@task
def query_user_following(
    user_login: str,
    github_credentials: GitHubCredentials,
    following_after: str = None,
    following_before: str = None,
    following_first: int = None,
    following_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).following(
        after=following_after,
        before=following_before,
        first=following_first,
        last=following_last,
    )

    if not return_fields:
        op_stack = ("user", "following")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["following"]


@task
def query_user_gist(
    user_login: str,
    gist_name: str,
    github_credentials: GitHubCredentials,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).gist(name=gist_name)

    if not return_fields:
        op_stack = ("user", "gist")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["gist"]


@task
def query_user_gist_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    gist_comments_after: str = None,
    gist_comments_before: str = None,
    gist_comments_first: int = None,
    gist_comments_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).gist_comments(
        after=gist_comments_after,
        before=gist_comments_before,
        first=gist_comments_first,
        last=gist_comments_last,
    )

    if not return_fields:
        op_stack = ("user", "gistComments")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["gist_comments"]


@task
def query_user_gists(
    user_login: str,
    github_credentials: GitHubCredentials,
    gists_privacy: graphql_schema.GistPrivacy = None,
    gists_order_by: graphql_schema.GistOrder = None,
    gists_after: str = None,
    gists_before: str = None,
    gists_first: int = None,
    gists_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).gists(
        privacy=gists_privacy,
        order_by=gists_order_by,
        after=gists_after,
        before=gists_before,
        first=gists_first,
        last=gists_last,
    )

    if not return_fields:
        op_stack = ("user", "gists")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["gists"]


@task
def query_user_interaction_ability(
    user_login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login)

    if not return_fields:
        op_stack = ("user", "interactionAbility")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["interaction_ability"]


@task
def query_user_issue_comments(
    user_login: str,
    github_credentials: GitHubCredentials,
    issue_comments_order_by: graphql_schema.IssueCommentOrder = None,
    issue_comments_after: str = None,
    issue_comments_before: str = None,
    issue_comments_first: int = None,
    issue_comments_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).issue_comments(
        order_by=issue_comments_order_by,
        after=issue_comments_after,
        before=issue_comments_before,
        first=issue_comments_first,
        last=issue_comments_last,
    )

    if not return_fields:
        op_stack = ("user", "issueComments")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["issue_comments"]


@task
def query_user_issues(
    user_login: str,
    issues_labels: str,
    issues_states: List[graphql_schema.IssueState],
    github_credentials: GitHubCredentials,
    issues_order_by: graphql_schema.IssueOrder = None,
    issues_filter_by: graphql_schema.IssueFilters = None,
    issues_after: str = None,
    issues_before: str = None,
    issues_first: int = None,
    issues_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).issues(
        order_by=issues_order_by,
        labels=issues_labels,
        states=issues_states,
        filter_by=issues_filter_by,
        after=issues_after,
        before=issues_before,
        first=issues_first,
        last=issues_last,
    )

    if not return_fields:
        op_stack = ("user", "issues")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["issues"]


@task
def query_user_organization(
    user_login: str,
    organization_login: str,
    github_credentials: GitHubCredentials,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).organization(login=organization_login)

    if not return_fields:
        op_stack = ("user", "organization")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["organization"]


@task
def query_user_organizations(
    user_login: str,
    github_credentials: GitHubCredentials,
    organizations_after: str = None,
    organizations_before: str = None,
    organizations_first: int = None,
    organizations_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).organizations(
        after=organizations_after,
        before=organizations_before,
        first=organizations_first,
        last=organizations_last,
    )

    if not return_fields:
        op_stack = ("user", "organizations")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["organizations"]


@task
def query_user_public_keys(
    user_login: str,
    github_credentials: GitHubCredentials,
    public_keys_after: str = None,
    public_keys_before: str = None,
    public_keys_first: int = None,
    public_keys_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).public_keys(
        after=public_keys_after,
        before=public_keys_before,
        first=public_keys_first,
        last=public_keys_last,
    )

    if not return_fields:
        op_stack = ("user", "publicKeys")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["public_keys"]


@task
def query_user_pull_requests(
    user_login: str,
    pull_requests_states: List[graphql_schema.PullRequestState],
    pull_requests_labels: str,
    github_credentials: GitHubCredentials,
    pull_requests_head_ref_name: str = None,
    pull_requests_base_ref_name: str = None,
    pull_requests_order_by: graphql_schema.IssueOrder = None,
    pull_requests_after: str = None,
    pull_requests_before: str = None,
    pull_requests_first: int = None,
    pull_requests_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).pull_requests(
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
        op_stack = ("user", "pullRequests")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["pull_requests"]


@task
def query_user_repositories_contributed_to(
    user_login: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).repositories_contributed_to(
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
        op_stack = ("user", "repositoriesContributedTo")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["repositories_contributed_to"]


@task
def query_user_saved_replies(
    user_login: str,
    github_credentials: GitHubCredentials,
    saved_replies_after: str = None,
    saved_replies_before: str = None,
    saved_replies_first: int = None,
    saved_replies_last: int = None,
    saved_replies_order_by: graphql_schema.SavedReplyOrder = {
        "field": "UPDATED_AT",
        "direction": "DESC",
    },
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).saved_replies(
        after=saved_replies_after,
        before=saved_replies_before,
        first=saved_replies_first,
        last=saved_replies_last,
        order_by=saved_replies_order_by,
    )

    if not return_fields:
        op_stack = ("user", "savedReplies")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["saved_replies"]


@task
def query_user_starred_repositories(
    user_login: str,
    github_credentials: GitHubCredentials,
    starred_repositories_after: str = None,
    starred_repositories_before: str = None,
    starred_repositories_first: int = None,
    starred_repositories_last: int = None,
    starred_repositories_owned_by_viewer: bool = None,
    starred_repositories_order_by: graphql_schema.StarOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).starred_repositories(
        after=starred_repositories_after,
        before=starred_repositories_before,
        first=starred_repositories_first,
        last=starred_repositories_last,
        owned_by_viewer=starred_repositories_owned_by_viewer,
        order_by=starred_repositories_order_by,
    )

    if not return_fields:
        op_stack = ("user", "starredRepositories")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["starred_repositories"]


@task
def query_user_status(
    user_login: str, github_credentials: GitHubCredentials, **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login)

    if not return_fields:
        op_stack = ("user", "status")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["status"]


@task
def query_user_top_repositories(
    user_login: str,
    top_repositories_order_by: graphql_schema.RepositoryOrder,
    github_credentials: GitHubCredentials,
    top_repositories_after: str = None,
    top_repositories_before: str = None,
    top_repositories_first: int = None,
    top_repositories_last: int = None,
    top_repositories_since: datetime = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).top_repositories(
        after=top_repositories_after,
        before=top_repositories_before,
        first=top_repositories_first,
        last=top_repositories_last,
        order_by=top_repositories_order_by,
        since=top_repositories_since,
    )

    if not return_fields:
        op_stack = ("user", "topRepositories")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["top_repositories"]


@task
def query_user_watching(
    user_login: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.user(login=user_login).watching(
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
        op_stack = ("user", "watching")
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["user"]["watching"]
