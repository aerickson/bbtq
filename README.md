# btq

Barebones TOML query. Like jq, but for TOML instead of JSON.

[![Test Status](https://github.com/aerickson/btq/actions/workflows/test.yml/badge.svg)](https://github.com/aerickson/btq/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/aerickson/btq/badge.svg?branch=master)](https://coveralls.io/github/aerickson/btq?branch=master)

## requirements

Python 3 likely

## installation

`pip3 install git+https://github.com/aerickson/btq.git@master`

## usage

```bash
# a search of '.' shows the entire document
$ tq btq/tests/test.toml .
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002,]
connection_max = 5000
enabled = true

# retrieve items
$ tq btq/tests/test.toml .title
TOML Example
$ tq btq/tests/test.toml .database.ports
[8001, 8001, 8002]

# retreive an array element
$ tq btq/tests/test.toml ".database.ports[2]"
8002

# can also be used via pipe
$ cat btq/tests/test.toml | ./bin/tq - .
```

## known limitations

- supports a subset of yq filter syntax
  - https://mikefarah.gitbook.io/yq/usage/path-expressions
  - doesn't support pipe operator

## why

- I couldn't get yq's experimental support for TOML working.
- I wanted a python implementation, all others seem to use go.

## development

### todo

- rename binary to btq (users can alias if they want at tq)
- more non-subprocess tests
- use a release tool that does more?
  - https://github.com/c4urself/bump2version/blob/master/RELATED.md
  - https://pypi.org/project/changes/

### incrementing version

Do this on master once the PR has landed.

`bump2version --dry-run --verbose major`

## links

- jq: https://github.com/stedolan/jq
- yq: https://github.com/kislyuk/yq
