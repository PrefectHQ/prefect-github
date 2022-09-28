from . import _version
from .credentials import GitHubCredentials  # noqa
from .filesystem import GitHubRepository  # noqa

__version__ = _version.get_versions()["version"]
