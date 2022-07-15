# bbtq development

## setup and testing

```bash
# install poetry if not already installed
# - use a preview version
curl -sSL https://install.python-poetry.org | POETRY_PREVIEW=1 python3 -

# open a poetry shell virtualenv
poetry shell

# install deps
poetry install --with=dev

# run cli
poetry run tq

# test
pytest
```

## TODO

- rename binary to bbtq (users can alias if they want at tq)
- more non-subprocess tests
- use a release tool that does more?
  - https://github.com/c4urself/bump2version/blob/master/RELATED.md
  - https://pypi.org/project/changes/

## incrementing version

Set in pyproject.toml at [tool.poetry.version].

Follow semantic versioning.

## publishing

```bash
## setup
#
# test.pypi setup
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi YOUR_TOKEN

## publishing to test server (https://test.pypi.org/)
#
# set a version that doesn't exist on test (can be lower, doesn't matter)
poetry build
poetry publish --dry-run -r test-pypi
poetry publish -r test-pypi
# go to https://test.pypi.org/project/bbtq
# find version just uploaded
# pip3 install outside of venv
# test it's workings

## publish for real
#
# set the version for real
rm -rf dist/
poetry build
# verify version is good
poetry publish --dry-run  # remove --dry-run to do for real
```
