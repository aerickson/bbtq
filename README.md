# btq

A barebones python TOML processor (like jq, but for toml).

[![Build Status](https://travis-ci.com/aerickson/tq.svg?branch=master)](https://travis-ci.com/aerickson/tq) [![Coverage Status](https://coveralls.io/repos/github/aerickson/btq/badge.svg?branch=master)](https://coveralls.io/github/aerickson/btq?branch=master)

## requirements

Python 3 likely

## installation

`pip3 install git+https://github.com/aerickson/btq.git@master`

## usage

```bash
$ tq . test/test.toml
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002,]
connection_max = 5000
enabled = true
$ tq .title test/test.toml
TOML Example
$ tq .database.ports test/test.toml
[8001, 8001, 8002]
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
