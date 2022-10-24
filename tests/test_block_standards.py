import pytest
from prefect.testing.standard_test_suites import BlockStandardTestSuite

from prefect_github import GitHubCredentials, GitHubRepository


@pytest.mark.parametrize("block", [GitHubRepository, GitHubCredentials])
class TestAllBlocksAdhereToStandards(BlockStandardTestSuite):
    @pytest.fixture
    def block(self, block):
        return block
