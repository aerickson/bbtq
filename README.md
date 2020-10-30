# btq

Barebones TOML query. Like jq, but for TOML instead of JSON.

[![Build Status](https://travis-ci.com/aerickson/btq.svg?branch=master)](https://travis-ci.com/aerickson/btq) [![Coverage Status](https://coveralls.io/repos/github/aerickson/btq/badge.svg?branch=master)](https://coveralls.io/github/aerickson/btq?branch=master)

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
$ tq ".database.ports[2]" btq/tests/test.toml
8002

# can also be used via pipe
$ cat btq/tests/test.toml | ./bin/tq - .
```

## known limitations

- supports a limited filter syntax
  - doesn't support pipe operator

## todo

- rename binary to btq (users can alias if they want at tq)
- more non-subprocess tests

## why

- I couldn't get yq's experimental support for TOML working.
- I wanted a python implementation, all others seem to use go.

## links

- jq: https://github.com/stedolan/jq
- yq: https://github.com/kislyuk/yq
