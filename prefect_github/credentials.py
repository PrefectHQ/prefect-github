"""Credential classes used to perform authenticated interactions with GitHub"""

from prefect.blocks.core import Block
from pydantic import SecretStr
from sgqlc.endpoint.http import HTTPEndpoint


class GitHubCredentials(Block):
    """
    Block used to manage GitHub authentication.

    Attributes:
        token: the token to authenticate into GitHub.

    Examples:
        Load stored GitHub credentials:
        ```python
        from prefect_github import GitHubCredentials
        github_credentials_block = GitHubCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "GitHub Credentials"
    # _logo_url = "<LOGO_URL_HERE>"  # noqa

    token: SecretStr = None

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
                token = "token_xxxxxxx"
                github_credentials = GitHubCredentials(token=token)
                endpoint = github_credentials.get_endpoint()
                return endpoint

            example_get_endpoint_flow()
            ```
        """
        if self.token is not None:
            base_headers = {"Authorization": f"Bearer {self.token.get_secret_value()}"}
        else:
            base_headers = None
        endpoint = HTTPEndpoint(
            "https://api.github.com/graphql", base_headers=base_headers
        )
        return endpoint
