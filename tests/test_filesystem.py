from prefect_github.filesystem import GitHub
from prefect_github import GitHubCredentials
import prefect_github
import pytest
from prefect.testing.utilities import AsyncMock
from prefect_github.exceptions import InvalidRepositoryURLError
import warnings

@pytest.fixture
def credential():
    return GitHubCredentials(token="XYZ")
    
class TestGitHub:
    async def test_subprocess_errors_are_surfaced(self):
        g = GitHub(repository="incorrect-url-scheme")
        with pytest.raises(
            OSError, match="fatal: repository 'incorrect-url-scheme' does not exist"
        ):
            await g.get_directory()

    async def test_repository_default(self, monkeypatch):
        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        g = GitHub(repository="prefect")
        await g.get_directory()

        assert mock.await_count == 1
        assert f"git clone prefect" in mock.await_args[0][0]

    async def test_reference_default(self, monkeypatch):
        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        g = GitHub(repository="prefect", reference="2.0.0")
        await g.get_directory()

        assert mock.await_count == 1
        assert f"git clone prefect -b 2.0.0 --depth 1" in mock.await_args[0][0]

    async def test_token_added_correctly(self, monkeypatch, credential):
        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        g = GitHub(repository="https://github.com/PrefectHQ/prefect.git", credential=credential)
        await g.get_directory()
        assert mock.await_count == 1
        assert f"git clone https://XYZ@github.com/PrefectHQ/prefect.git" in mock.await_args[0][0]

    async def test_ssh_fails_with_credential(self, monkeypatch, credential):
        class p:
            returncode = 0

        mock = AsyncMock(return_value=p())
        monkeypatch.setattr(prefect_github.filesystem, "run_process", mock)
        with pytest.raises(ValueError):
            g = GitHub(repository="git@github.com:PrefectHQ/prefect.git", credential=credential)