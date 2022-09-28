import pytest
from prefect.testing.utilities import AsyncMock

import prefect_github
from prefect_github import GitHubCredentials
from prefect_github.filesystem import GitHub


class TestGitHub:
    async def test_subprocess_errors_are_surfaced(self):
        """Ensure that errors from GitHub are being surfaced to users."""
        g = GitHub(repository="incorrect-url-scheme")
        with pytest.raises(
            OSError, match="fatal: repository 'incorrect-url-scheme' does not exist"
        ):
            await g.get_directory()

    async def test_repository_default(self, monkeypatch):
        """Ensure that default command is 'git clone <repo name>' when given just
        a repo.
        """

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        g = GitHub(repository="prefect")
        await g.get_directory()

        assert mock.await_count == 1
        assert "git clone prefect" in mock.await_args[0][0]

    async def test_reference_default(self, monkeypatch):
        """Ensure that default command is 'git clone <repo name> -b <reference> --depth 1'  # noqa: E501
        when just a repository and reference are given.
        """

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        g = GitHub(repository="prefect", reference="2.0.0")
        await g.get_directory()

        assert mock.await_count == 1
        assert "git clone prefect -b 2.0.0 --depth 1" in mock.await_args[0][0]

    async def test_token_added_correctly(self, monkeypatch):
        """Ensure that the repo url is in the format `https://<oauth-key>@github.com/<username>/<repo>.git`."""  # noqa: E501

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        credential = GitHubCredentials(token="XYZ")
        g = GitHub(
            repository="https://github.com/PrefectHQ/prefect.git", credential=credential
        )
        await g.get_directory()
        assert mock.await_count == 1
        assert (
            "git clone https://XYZ@github.com/PrefectHQ/prefect.git"
            in mock.await_args[0][0]
        )

    async def test_ssh_fails_with_credential(self, monkeypatch):
        """Ensure that credentials cannot be passed in with an SSH URL."""

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        credential = GitHubCredentials(token="XYZ")
        with pytest.raises(ValueError):
            GitHub(
                repository="git@github.com:PrefectHQ/prefect.git", credential=credential
            )
