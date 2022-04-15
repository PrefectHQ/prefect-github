from . import _version
from .credentials import GitHubCredentials  # noqa

__version__ = _version.get_versions()["version"]
