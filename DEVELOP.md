# bbtq development

## todo

- rename binary to bbtq (users can alias if they want at tq)
- more non-subprocess tests
- use a release tool that does more?
  - https://github.com/c4urself/bump2version/blob/master/RELATED.md
  - https://pypi.org/project/changes/

## incrementing version

Do this on master once the PR has landed.

`bump2version --dry-run --verbose major`

## publishing

Currently using hatch/hatchling.

see https://packaging.python.org/en/latest/tutorials/packaging-projects/ and
https://hatch.pypa.io/latest/publish/.
