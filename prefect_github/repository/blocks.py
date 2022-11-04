import io
from distutils.dir_util import copy_tree
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Optional, Tuple, Union
from urllib.parse import urlparse, urlunparse

from prefect.filesystems import ReadableDeploymentStorage
from prefect.utilities.asyncutils import sync_compatible
from prefect.utilities.processutils import run_process
from pydantic import Field, validator

from prefect_github import GitHubCredentials
from prefect_github.exceptions import InvalidRepositoryURLError


class GitHubRepository(ReadableDeploymentStorage):
    """
    Interact with files stored on GitHub repositories.
    """

    _block_type_name = "GitHub Repository"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/187oCWsD18m5yooahq1vU0/ace41e99ab6dc40c53e5584365a33821/github.png?h=250"  # noqa: E501

    repository_url: str = Field(
        default=...,
        title="Repository URL",
        description=(
            "The URL of a GitHub repository to read from, in either HTTPS or SSH "
            "format. If you are using a private repo, it must be in the HTTPS format."
        ),
    )
    reference: Optional[str] = Field(
        default=None,
        description="An optional reference to pin to; can be a branch name or tag.",
    )
    credentials: Optional[GitHubCredentials] = Field(
        default=None,
        description="An optional GitHubCredentials block for using private GitHub repos.",  # noqa: E501
    )

    @validator("credentials")
    def _ensure_credentials_go_with_https(cls, v: str, values: dict):
        """Ensure that credentials are not provided with 'SSH' formatted GitHub URLs."""
        if v is not None:
            if urlparse(values["repository_url"]).scheme != "https":
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

    def _create_repo_url(self) -> str:
        """Format the URL provided to the `git clone` command.

        For private repos: https://<oauth-key>@github.com/<username>/<repo>.git
        All other repos should be the same as `self.repository`.
        """
        url_components = urlparse(self.repository_url)
        if url_components.scheme == "https" and self.credentials is not None:
            token_value = self.credentials.token.get_secret_value()
            updated_components = url_components._replace(
                netloc=f"{token_value}@{url_components.netloc}"
            )
            full_url = urlunparse(updated_components)
        else:
            full_url = self.repository_url

        return full_url

    @staticmethod
    def _get_paths(
        dst_dir: Union[str, None], src_dir: str, sub_directory: str
    ) -> Tuple[str, str]:
        """Returns the fully formed paths for GitHubRepository contents in the form
        (content_source, content_destination).
        """
        if dst_dir is None:
            content_destination = Path(".").absolute()
        else:
            content_destination = Path(dst_dir)

        content_source = Path(src_dir)

        if sub_directory:
            content_destination = content_destination.joinpath(sub_directory)
            content_source = content_source.joinpath(sub_directory)

        return str(content_source), str(content_destination)

    @sync_compatible
    async def get_directory(
        self, from_path: Optional[str] = None, local_path: Optional[str] = None
    ) -> None:
        """
        Clones a GitHub project specified in `from_path` to the provided `local_path`;
        defaults to cloning the repository reference configured on the Block to the
        present working directory.

        Args:
            from_path: If provided, interpreted as a subdirectory of the underlying
                repository that will be copied to the provided local path.
            local_path: A local path to clone to; defaults to present working directory.
        """
        # CONSTRUCT COMMAND
        cmd = f"git clone {self._create_repo_url()}"
        if self.reference:
            cmd += f" -b {self.reference}"

        # Limit git history
        cmd += " --depth 1"

        # Clone to a temporary directory and move the subdirectory over
        with TemporaryDirectory(suffix="prefect") as tmp_dir:
            tmp_path_str = tmp_dir
            cmd += f" {tmp_path_str}"

            err_stream = io.StringIO()
            out_stream = io.StringIO()
            process = await run_process(cmd, stream_output=(out_stream, err_stream))
            if process.returncode != 0:
                err_stream.seek(0)
                raise RuntimeError(f"Failed to pull from remote:\n {err_stream.read()}")

            content_source, content_destination = self._get_paths(
                dst_dir=local_path, src_dir=tmp_path_str, sub_directory=from_path
            )

            copy_tree(src=content_source, dst=content_destination)
