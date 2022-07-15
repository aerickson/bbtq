# bbtq development

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
```

## TODO

- rename binary to bbtq (users can alias if they want at tq)
- more non-subprocess tests
- use a release tool that does more?
  - https://github.com/c4urself/bump2version/blob/master/RELATED.md
  - https://pypi.org/project/changes/

## incrementing version

Do this on master once the PR has landed.

`bump2version --dry-run --verbose major`

## publishing

Currently using hatch (and pipenv for dev deps).

TODO: Switch to poetry for all?

see https://packaging.python.org/en/latest/tutorials/packaging-projects/ and
https://hatch.pypa.io/latest/publish/.
