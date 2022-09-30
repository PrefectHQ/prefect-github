from pathlib import Path
from unittest.mock import Mock

import pytest
from prefect.testing.utilities import AsyncMock

import prefect_github
from prefect_github import GitHubCredentials
from prefect_github.repository import GitHubRepository


class TestGitHub:
    async def test_subprocess_errors_are_surfaced(self):
        """Ensure that errors from GitHub are being surfaced to users."""
        g = GitHubRepository(repository="incorrect-url-scheme")
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
        monkeypatch.setattr(prefect_github.repository, "run_process", mock)
        g = GitHubRepository(repository="prefect")
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
        monkeypatch.setattr(prefect_github.repository, "run_process", mock)
        g = GitHubRepository(repository="prefect", reference="2.0.0")
        await g.get_directory()

        assert mock.await_count == 1
        assert "git clone prefect -b 2.0.0 --depth 1" in mock.await_args[0][0]

    async def test_token_added_correctly_from_credential(self, monkeypatch):
        """Ensure that the repo url is in the format `https://<oauth-key>@github.com/<username>/<repo>.git`."""  # noqa: E501

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.repository, "run_process", mock)
        credential = GitHubCredentials(token="XYZ")
        g = GitHubRepository(
            repository="https://github.com/PrefectHQ/prefect.git",
            credentials=credential,
        )
        await g.get_directory()
        assert mock.await_count == 1
        assert (
            "git clone https://XYZ@github.com/PrefectHQ/prefect.git"
            in mock.await_args[0][0]
        )

    async def test_ssh_fails_with_credential(self, monkeypatch):
        """Ensure that credentials cannot be passed in if the URL is not in the HTTPS
        format.
        """

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.repository, "run_process", mock)
        credential = GitHubCredentials(token="XYZ")
        with pytest.raises(ValueError):
            GitHubRepository(
                repository="git@github.com:PrefectHQ/prefect.git",
                credentials=credential,
            )

    async def test_files_moved_correctly_with_default(self, monkeypatch):
        """Ensure copytree called with correct arguments."""

        class p:
            returncode = 0

        mock_run_process = AsyncMock(return_value=p())
        mock_copytree = Mock()
        mock_tmp_dir = Mock()
        mock_tmp_dir.name = "test"
        monkeypatch.setattr(
            prefect_github.repository,
            "TemporaryDirectory",
            Mock(return_value=mock_tmp_dir),
        )
        monkeypatch.setattr(prefect_github.repository, "run_process", mock_run_process)
        monkeypatch.setattr(prefect_github.repository, "copytree", mock_copytree)
        g = GitHubRepository(repository="prefect", reference="2.0.0")
        await g.get_directory()

        assert mock_copytree.mock_calls[0].kwargs["src"] == "test"
        assert mock_copytree.mock_calls[0].kwargs["dst"] == Path.cwd()

    async def test_files_moved_correctly_with_from_path(self, monkeypatch):
        """Ensure copytree called with correct arguments when `from_path` parameter
        is supplied.
        """

        class p:
            returncode = 0

        TMP_DIR_NAME = "test"
        mock_run_process = AsyncMock(return_value=p())
        mock_copytree = Mock()
        mock_tmp_dir = Mock()
        mock_tmp_dir.name = TMP_DIR_NAME
        monkeypatch.setattr(
            prefect_github.repository,
            "TemporaryDirectory",
            Mock(return_value=mock_tmp_dir),
        )
        monkeypatch.setattr(prefect_github.repository, "run_process", mock_run_process)
        monkeypatch.setattr(prefect_github.repository, "copytree", mock_copytree)

        g = GitHubRepository(repository="prefect", reference="2.0.0")
        from_path = "dog-path"
        await g.get_directory(from_path=from_path)

        assert (
            mock_copytree.mock_calls[0].kwargs["src"] == TMP_DIR_NAME + "/" + from_path
        )
        assert mock_copytree.mock_calls[0].kwargs["dst"] == Path.cwd() / from_path
