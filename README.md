# prefect-github

## Welcome!

Prefect integrations for interacting with GitHub

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

### Write and run a flow

```python
from prefect import flow
from prefect_github import GitHubCredentials
from prefect_github.repository import query_repository
from prefect_github.mutations import create_issue

@flow
def example_flow():
    token = "ghp_token"
    github_credentials = GitHubCredentials(token)
    repository_id = query_repository("owner", "repository", github_credentials, id=True).result()["id"]
    issue = create_issue(repository_id, "title", assignee_ids="", label_ids="", project_ids="", github_credentials=github_credentials)
    return issue

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-github`, feel free to open an issue in the [prefect-github](https://github.com/PrefectHQ/prefect-github) repository.

If you have any questions or issues while using `prefect-github`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-github` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-github.git

cd prefect-github/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
