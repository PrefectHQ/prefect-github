# prefect-github
 
<p align="center">
    <a href="https://pypi.python.org/pypi/prefect-github/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-github?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-github/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-github?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-github/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-github?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-github/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-github?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

Prefect integrations interacting with GitHub.

The tasks within this collection were created by a code generator using the GitHub GraphQL schema.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-github` with `pip`:

```bash
pip install prefect-github
```

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m prefect_github
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

### Write and run a flow

```python
from prefect import flow
from prefect_github import GitHubCredentials
from prefect_github.repository import query_repository
from prefect_github.mutations import add_star_starrable


@flow()
def github_add_star_flow():
    github_credentials = GitHubCredentials.load("github-token")
    repository_id = query_repository(
        "PrefectHQ",
        "Prefect",
        github_credentials=github_credentials,
        return_fields="id"
    )["id"]
    starrable = add_star_starrable(
        repository_id,
        github_credentials
    )
    return starrable


github_add_star_flow()
```

## Resources

If you encounter any bugs while using `prefect-github`, feel free to open an issue in the [prefect-github](https://github.com/PrefectHQ/prefect-github) repository.

If you have any questions or issues while using `prefect-github`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`prefect-github`](https://github.com/PrefectHQ/prefect-github) for updates too!

## Development

If you'd like to install a version of `prefect-github` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-github.git

cd prefect-github/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
