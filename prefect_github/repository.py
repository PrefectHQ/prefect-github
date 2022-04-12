"""This is a module for interacting with GitHub repository tasks"""

from datetime import datetime
from pathlib import Path
from typing import List

from prefect import task
from sgqlc.operation import Operation

from prefect_github import GitHubCredentials
from prefect_github.schemas import graphql_schema
from prefect_github.utils import initialize_return_fields_defaults

config_path = Path("configs") / "query" / "repository.json"
return_fields_defaults = initialize_return_fields_defaults(config_path)


@task
def query_repository(
    owner: str,
    name: str,
    github_credentials: GitHubCredentials,
    follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(owner=owner, name=name, follow_renames=follow_renames)

    if not return_fields:
        op_stack = ["repository"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]


@task
def query_repository_project(
    repository_owner: str,
    repository_name: str,
    project_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).project(number=project_number)

    if not return_fields:
        op_stack = ["repository", "project"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["project"]


@task
def query_repository_projects(
    repository_owner: str,
    repository_name: str,
    projects_states: List[graphql_schema.ProjectState],
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
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
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).projects(
        order_by=projects_order_by,
        search=projects_search,
        states=projects_states,
        after=projects_after,
        before=projects_before,
        first=projects_first,
        last=projects_last,
    )

    if not return_fields:
        op_stack = ["repository", "projects"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["projects"]


@task
def query_repository_packages(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "packages"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["packages"]


@task
def query_repository_stargazers(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    stargazers_after: str = None,
    stargazers_before: str = None,
    stargazers_first: int = None,
    stargazers_last: int = None,
    stargazers_order_by: graphql_schema.StarOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "stargazers"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["stargazers"]


@task
def query_repository_license_info(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "licenseInfo"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["licenseInfo"]


@task
def query_repository_owner(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "owner"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["owner"]


@task
def query_repository_assignable_users(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    assignable_users_query: str = None,
    assignable_users_after: str = None,
    assignable_users_before: str = None,
    assignable_users_first: int = None,
    assignable_users_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "assignableUsers"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["assignableUsers"]


@task
def query_repository_branch_protection_rules(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    branch_protection_rules_after: str = None,
    branch_protection_rules_before: str = None,
    branch_protection_rules_first: int = None,
    branch_protection_rules_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "branchProtectionRules"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["branchProtectionRules"]


@task
def query_repository_code_of_conduct(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "codeOfConduct"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["codeOfConduct"]


@task
def query_repository_collaborators(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    collaborators_affiliation: graphql_schema.CollaboratorAffiliation = None,
    collaborators_query: str = None,
    collaborators_after: str = None,
    collaborators_before: str = None,
    collaborators_first: int = None,
    collaborators_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "collaborators"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["collaborators"]


@task
def query_repository_commit_comments(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    commit_comments_after: str = None,
    commit_comments_before: str = None,
    commit_comments_first: int = None,
    commit_comments_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "commitComments"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["commitComments"]


@task
def query_repository_contact_links(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "contactLinks"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["contactLinks"]


@task
def query_repository_default_branch_ref(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "defaultBranchRef"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["defaultBranchRef"]


@task
def query_repository_deploy_keys(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    deploy_keys_after: str = None,
    deploy_keys_before: str = None,
    deploy_keys_first: int = None,
    deploy_keys_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "deployKeys"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["deployKeys"]


@task
def query_repository_deployments(
    repository_owner: str,
    repository_name: str,
    deployments_environments: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    deployments_order_by: graphql_schema.DeploymentOrder = {
        "field": "CREATED_AT",
        "direction": "ASC",
    },
    deployments_after: str = None,
    deployments_before: str = None,
    deployments_first: int = None,
    deployments_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "deployments"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["deployments"]


@task
def query_repository_discussion(
    repository_owner: str,
    repository_name: str,
    discussion_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).discussion(number=discussion_number)

    if not return_fields:
        op_stack = ["repository", "discussion"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["discussion"]


@task
def query_repository_discussion_categories(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    discussion_categories_after: str = None,
    discussion_categories_before: str = None,
    discussion_categories_first: int = None,
    discussion_categories_last: int = None,
    discussion_categories_filter_by_assignable: bool = False,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "discussionCategories"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["discussionCategories"]


@task
def query_repository_discussions(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "discussions"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["discussions"]


@task
def query_repository_environment(
    repository_owner: str,
    repository_name: str,
    environment_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).environment(name=environment_name)

    if not return_fields:
        op_stack = ["repository", "environment"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["environment"]


@task
def query_repository_environments(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    environments_after: str = None,
    environments_before: str = None,
    environments_first: int = None,
    environments_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "environments"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["environments"]


@task
def query_repository_forks(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "forks"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["forks"]


@task
def query_repository_funding_links(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "fundingLinks"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["fundingLinks"]


@task
def query_repository_interaction_ability(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "interactionAbility"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["interactionAbility"]


@task
def query_repository_issue(
    repository_owner: str,
    repository_name: str,
    issue_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issue(number=issue_number)

    if not return_fields:
        op_stack = ["repository", "issue"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["issue"]


@task
def query_repository_issue_or_pull_request(
    repository_owner: str,
    repository_name: str,
    issue_or_pull_request_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issue_or_pull_request(number=issue_or_pull_request_number)

    if not return_fields:
        op_stack = ["repository", "issueOrPullRequest"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["issueOrPullRequest"]


@task
def query_repository_issue_templates(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "issueTemplates"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["issueTemplates"]


@task
def query_repository_issues(
    repository_owner: str,
    repository_name: str,
    issues_labels: str,
    issues_states: List[graphql_schema.IssueState],
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
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
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).issues(
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
        op_stack = ["repository", "issues"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["issues"]


@task
def query_repository_label(
    repository_owner: str,
    repository_name: str,
    label_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).label(name=label_name)

    if not return_fields:
        op_stack = ["repository", "label"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["label"]


@task
def query_repository_labels(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
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
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "labels"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["labels"]


@task
def query_repository_languages(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    languages_after: str = None,
    languages_before: str = None,
    languages_first: int = None,
    languages_last: int = None,
    languages_order_by: graphql_schema.LanguageOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "languages"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["languages"]


@task
def query_repository_latest_release(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "latestRelease"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["latestRelease"]


@task
def query_repository_mentionable_users(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    mentionable_users_query: str = None,
    mentionable_users_after: str = None,
    mentionable_users_before: str = None,
    mentionable_users_first: int = None,
    mentionable_users_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "mentionableUsers"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["mentionableUsers"]


@task
def query_repository_milestone(
    repository_owner: str,
    repository_name: str,
    milestone_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).milestone(number=milestone_number)

    if not return_fields:
        op_stack = ["repository", "milestone"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["milestone"]


@task
def query_repository_milestones(
    repository_owner: str,
    repository_name: str,
    milestones_states: List[graphql_schema.MilestoneState],
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    milestones_after: str = None,
    milestones_before: str = None,
    milestones_first: int = None,
    milestones_last: int = None,
    milestones_order_by: graphql_schema.MilestoneOrder = None,
    milestones_query: str = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).milestones(
        after=milestones_after,
        before=milestones_before,
        first=milestones_first,
        last=milestones_last,
        states=milestones_states,
        order_by=milestones_order_by,
        query=milestones_query,
    )

    if not return_fields:
        op_stack = ["repository", "milestones"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["milestones"]


@task
def query_repository_object(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    object_oid: datetime = None,
    object_expression: str = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).object(oid=object_oid, expression=object_expression)

    if not return_fields:
        op_stack = ["repository", "object"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["object"]


@task
def query_repository_pinned_discussions(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    pinned_discussions_after: str = None,
    pinned_discussions_before: str = None,
    pinned_discussions_first: int = None,
    pinned_discussions_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "pinnedDiscussions"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["pinnedDiscussions"]


@task
def query_repository_pinned_issues(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    pinned_issues_after: str = None,
    pinned_issues_before: str = None,
    pinned_issues_first: int = None,
    pinned_issues_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "pinnedIssues"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["pinnedIssues"]


@task
def query_repository_primary_language(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "primaryLanguage"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["primaryLanguage"]


@task
def query_repository_project_next(
    repository_owner: str,
    repository_name: str,
    project_next_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).project_next(number=project_next_number)

    if not return_fields:
        op_stack = ["repository", "projectNext"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["projectNext"]


@task
def query_repository_projects_next(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
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
        op_stack = ["repository", "projectsNext"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["projectsNext"]


@task
def query_repository_pull_request(
    repository_owner: str,
    repository_name: str,
    pull_request_number: int,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).pull_request(number=pull_request_number)

    if not return_fields:
        op_stack = ["repository", "pullRequest"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["pullRequest"]


@task
def query_repository_pull_request_templates(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    )

    if not return_fields:
        op_stack = ["repository", "pullRequestTemplates"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["pullRequestTemplates"]


@task
def query_repository_pull_requests(
    repository_owner: str,
    repository_name: str,
    pull_requests_states: List[graphql_schema.PullRequestState],
    pull_requests_labels: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
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
        op_stack = ["repository", "pullRequests"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["pullRequests"]


@task
def query_repository_ref(
    repository_owner: str,
    repository_name: str,
    ref_qualified_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).ref(qualified_name=ref_qualified_name)

    if not return_fields:
        op_stack = ["repository", "ref"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["ref"]


@task
def query_repository_refs(
    repository_owner: str,
    repository_name: str,
    refs_ref_prefix: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    refs_query: str = None,
    refs_after: str = None,
    refs_before: str = None,
    refs_first: int = None,
    refs_last: int = None,
    refs_direction: graphql_schema.OrderDirection = None,
    refs_order_by: graphql_schema.RefOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).refs(
        query=refs_query,
        after=refs_after,
        before=refs_before,
        first=refs_first,
        last=refs_last,
        ref_prefix=refs_ref_prefix,
        direction=refs_direction,
        order_by=refs_order_by,
    )

    if not return_fields:
        op_stack = ["repository", "refs"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["refs"]


@task
def query_repository_release(
    repository_owner: str,
    repository_name: str,
    release_tag_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).release(tag_name=release_tag_name)

    if not return_fields:
        op_stack = ["repository", "release"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["release"]


@task
def query_repository_releases(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    releases_after: str = None,
    releases_before: str = None,
    releases_first: int = None,
    releases_last: int = None,
    releases_order_by: graphql_schema.ReleaseOrder = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "releases"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["releases"]


@task
def query_repository_repository_topics(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    repository_topics_after: str = None,
    repository_topics_before: str = None,
    repository_topics_first: int = None,
    repository_topics_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "repositoryTopics"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["repositoryTopics"]


@task
def query_repository_submodules(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    submodules_after: str = None,
    submodules_before: str = None,
    submodules_first: int = None,
    submodules_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "submodules"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["submodules"]


@task
def query_repository_vulnerability_alerts(
    repository_owner: str,
    repository_name: str,
    vulnerability_alerts_states: List[graphql_schema.RepositoryVulnerabilityAlertState],
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    vulnerability_alerts_after: str = None,
    vulnerability_alerts_before: str = None,
    vulnerability_alerts_first: int = None,
    vulnerability_alerts_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

    op = Operation(graphql_schema.Query)
    op_settings = op.repository(
        owner=repository_owner,
        name=repository_name,
        follow_renames=repository_follow_renames,
    ).vulnerability_alerts(
        after=vulnerability_alerts_after,
        before=vulnerability_alerts_before,
        first=vulnerability_alerts_first,
        last=vulnerability_alerts_last,
        states=vulnerability_alerts_states,
    )

    if not return_fields:
        op_stack = ["repository", "vulnerabilityAlerts"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["vulnerabilityAlerts"]


@task
def query_repository_watchers(
    repository_owner: str,
    repository_name: str,
    github_credentials: GitHubCredentials,
    repository_follow_renames: bool = True,
    watchers_after: str = None,
    watchers_before: str = None,
    watchers_first: int = None,
    watchers_last: int = None,
    **return_fields
) -> dict:
    endpoint = github_credentials.get_endpoint()

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
        op_stack = ["repository", "watchers"]
        return_fields = {
            return_field: True for return_field in return_fields_defaults[op_stack]
        }
    op_settings.__fields__(**return_fields)

    result = endpoint(op)
    return result["data"]["repository"]["watchers"]
