"""Credential classes used to perform authenticated interactions with GitHub"""

from dataclasses import dataclass

from sgqlc.endpoint.http import HTTPEndpoint


@dataclass
class GitHubCredentials:
    """
    Dataclass used to manage GitHub authentication.

    Args:
        token: the token to authenticate into GitHub.
    """

    token: str

    def get_endpoint(self) -> HTTPEndpoint:
        """
        Gets an authenticated GitHub GraphQL HTTPEndpoint.

        Returns:
            An authenticated GitHub GraphQL HTTPEndpoint

        Example:
            Gets an authenticated GitHub GraphQL HTTPEndpoint.
            ```python
            from prefect import flow
            from prefect_github import GitHubCredentials

            @flow
            def example_get_endpoint_flow():
                token = "consumer_key"
                github_credentials = GitHubCredentials(token)
                endpoint = github_credentials.get_endpoint()
                return endpoint

            example_get_endpoint_flow()
            ```
        """
        endpoint = HTTPEndpoint(
            "https://api.github.com/graphql", {"Authorization": f"Bearer {self.token}"}
        )
        return endpoint
