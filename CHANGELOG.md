# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## 0.1.2

Released on April 27th, 2022.

### Fixed

- Fix config JSON in egg by adding `include_package_data=True` in setup.py.

## 0.1.1

Released on April 27th, 2022.

### Fixed

- Fix missing modules in egg.

## 0.1.0

Released on April 27th, 2022.

### Added

- `execute_graphql`, `query_repository*`, `query_user*`, `query_viewer*`, `query_organization*`, `query_repository_owner*`, `add_comment*`, `create_pull_request`, `close_pull_request`, `create_issue`, `close_issue`, `add_star_starrable`, `remove_star_starrable`, `add_reaction*`, `remove_reaction*`, `request_reviews*` tasks - [#5](https://github.com/PrefectHQ/prefect-github/pull/5)
