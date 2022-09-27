"""The GitHub filesystem for Prefect"""
import io
import tempfile
from pathlib import Path
from typing import Optional

from prefect.filesystems import ReadableDeploymentStorage
from prefect.utilities.processutils import run_process
from pydantic import Field, validator

from prefect_github import GitHubCredentials
from prefect_github.errors import InvalidRepositoryURLError


class GitHub(ReadableDeploymentStorage):
    """
    Interact with files stored on GitHub repositories.
    """

    _block_type_name = "GitHub"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/187oCWsD18m5yooahq1vU0/ace41e99ab6dc40c53e5584365a33821/github.png?h=250"

    repository: str = Field(
        default=...,
        description=(
            "The URL of a GitHub repository to read from, in either HTTPS or SSH format. "
            "If you are using a private repo, it must be in the HTTPS format."
        ),
    )
    reference: Optional[str] = Field(
        default=None,
        description="An optional reference to pin to; can be a branch name or tag.",
    )
    credential: Optional[GitHubCredentials] = Field(
        default=None,
        description="An optional GitHubCredentials block for using private GitHub repos.",
    )

    @validator("credential")
    def ensure_credentials_go_with_https(cls, v: str, values: dict):
        """Ensure that credentials are not provided with 'SSH' formatted GitHub URLs."""
        if v is not None:
            if values["repository"].startswith("git@"):
                raise InvalidRepositoryURLError(
                    (
                        "Crendentials can only be used with GitHub repositories "
                        "using the 'HTTPS' format. You must either remove the "
                        "credential if you wish to use the 'SSH' format and are not "
                        "using a private repository, or you must change the repository "
                        "url to the 'HTTPS' format. "
                    )
                )

        return v

    def create_repo_url(self):
        """Format the URL provided to the `git clone` command.

        For private repos: https://oauth-key-goes-here@github.com/username/repo.git
        All other repos should be the same as `self.repository`.
        """

        if self.repository.startswith("https://") and self.credential is not None:
            repo_url = self.repository[8:]
            token_value = self.credential.token.get_secret_value()
            full_url = f"https://{token_value}@{repo_url}"
        else:
            full_url = self.repository

        return full_url

    async def get_directory(
        self, from_path: str = None, local_path: str = None
    ) -> None:
        """
        Clones a GitHub project specified in `from_path` to the provided `local_path`; defaults to cloning
        the repository reference configured on the Block to the present working directory.

        Args:
            from_path: If provided, interpreted as a subdirectory of the underlying repository that will
                be copied to the provided local path.
            local_path: A local path to clone to; defaults to present working directory.
        """

        # CONSTRUCT COMMAND
        cmd = "git clone"

        cmd += f" {self.create_repo_url()}"
        if self.reference:
            cmd += f" -b {self.reference} --depth 1"

        if local_path is None:
            local_path = Path(".").absolute()

        if not from_path:
            from_path = ""

        # in this case, we clone to a temporary directory and move the subdirectory over
        tmp_dir = None
        tmp_dir = tempfile.TemporaryDirectory(suffix="prefect")
        path_to_move = str(Path(tmp_dir.name).joinpath(from_path))
        cmd += f" {tmp_dir.name} && cp -R {path_to_move}/."

        cmd += f" {local_path}"

        try:
            err_stream = io.StringIO()
            out_stream = io.StringIO()
            process = await run_process(cmd, stream_output=(out_stream, err_stream))
        finally:
            if tmp_dir:
                tmp_dir.cleanup()

        if process.returncode != 0:
            err_stream.seek(0)
            raise OSError(f"Failed to pull from remote:\n {err_stream.read()}")
