import os
from pathlib import Path
from tempfile import TemporaryDirectory
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

    async def test_copy_contents_works(self, monkeypatch):
        """Sanity check for function to make sure that contents are moved as expected."""  # noqa

        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.repository, "run_process", mock)

        with TemporaryDirectory() as tmp_src:
            # add file to tmp_src
            f1_name = "dog.text"
            f1_path = Path(tmp_src) / f1_name
            f1 = open(f1_path, "w")
            f1.close()

            # add directory with file to tmp_src
            sub_dir_name = "puppy"
            sub_dir_path = Path(tmp_src) / sub_dir_name
            os.mkdir(sub_dir_path)

            f2_name = "cat.txt"
            f2_path = sub_dir_path / f2_name
            f2 = open(f2_path, "w")
            f2.close()

            expected_parent_contents = {f1_name, sub_dir_name}
            expected_child_contents = {f2_name}

            assert set(os.listdir(tmp_src)) == expected_parent_contents
            assert set(os.listdir(sub_dir_path)) == expected_child_contents

            # move file contents to tmp_dst
            with TemporaryDirectory() as tmp_dst:
                mock_get_paths = Mock(return_value=(tmp_src, tmp_dst))
                monkeypatch.setattr(
                    prefect_github.repository.GitHubRepository,
                    "_get_paths",
                    mock_get_paths,
                )

                g = GitHubRepository(
                    repository="https://github.com/PrefectHQ/prefect.git",
                )
                await g.get_directory()

                assert set(os.listdir(tmp_dst)) == expected_parent_contents
                assert (
                    set(os.listdir(Path(tmp_dst) / sub_dir_name))
                    == expected_child_contents
                )

    async def test_copy_contents_works_with_path(self):
        """Sanity check for function to make sure that contents are moved as expected
        when passing a sub-directory.
        """
        with TemporaryDirectory() as tmp_src:
            # add file to tmp_src
            f1_name = "dog.text"
            f1_path = Path(tmp_src) / f1_name
            f1 = open(f1_path, "w")
            f1.close()

            # add directory with file to tmp_src
            sub_dir_name = "puppy"
            sub_dir_path = Path(tmp_src) / sub_dir_name
            os.mkdir(sub_dir_path)

            f2_name = "cat.txt"
            f2_path = sub_dir_path / f2_name
            f2 = open(f2_path, "w")
            f2.close()

            expected_parent_contents = {f1_name, sub_dir_name}
            expected_child_contents = {f2_name}

            assert set(os.listdir(tmp_src)) == expected_parent_contents
            assert set(os.listdir(sub_dir_path)) == expected_child_contents
            breakpoint()
            # move file contents to tmp_dst
            with TemporaryDirectory() as tmp_dst:
                GitHubRepository._get_paths(
                    dst_dir=tmp_dst, src_dir=tmp_src, sub_directory=sub_dir_name
                )

                assert set(os.listdir(tmp_dst)) == expected_child_contents
