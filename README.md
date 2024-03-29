# bbtq

Barebones TOML query. Like jq, but for TOML instead of JSON.

<a href="https://pypi.org/project/bbtq/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bbtq"></a>
[![Test Status](https://github.com/aerickson/bbtq/actions/workflows/test.yml/badge.svg)](https://github.com/aerickson/bbtq/actions/workflows/test.yml)
[![Code Coverage](https://codecov.io/gh/aerickson/bbtq/branch/master/graph/badge.svg?token=y0FQaJuAJu)](https://codecov.io/gh/aerickson/bbtq)

## installation

```bash
# via pypi
pip3 install bbtq

# directly from repo
pip3 install git+https://github.com/aerickson/bbtq.git@master
```

## usage

```bash
# a search of '.' shows the entire document
$ tq bbtq/tests/test.toml .
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
$ tq bbtq/tests/test.toml .title
TOML Example
$ tq bbtq/tests/test.toml .database.ports
[8001, 8001, 8002]

# retreive an array element
$ tq bbtq/tests/test.toml ".database.ports[2]"
8002

# can also be used via pipe
$ cat bbtq/tests/test.toml | ./bin/tq - .
```

## known limitations

- supports a subset of jq's basic filter syntax
  - specifically: identity, object identifier-index, and array index
    - see https://stedolan.github.io/jq/manual/#Basicfilters

## why

I wanted something that was:

- minimal
- python
- standalone (python yq depends on jq)

## links

- jq: https://github.com/stedolan/jq
- yq (c): https://github.com/mikefarah/yq
- yq (python): https://github.com/kislyuk/yq
  - yq's `tomlq` works great and supports much more of jq's filter syntax
- tomlq (go): https://github.com/jamesmunns/tomlq
