# btq

A barebones python tq (like jq, but for toml).

[![Build Status](https://travis-ci.com/aerickson/tq.svg?branch=master)](https://travis-ci.com/aerickson/tq)

## requirements

Python 3 likely

## usage

```bash
$ ./tq . test/test.toml
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002,]
connection_max = 5000
enabled = true
$ ./tq .title test/test.toml
TOML Example
$ ./tq .database.ports test/test.toml
[8001, 8001, 8002]
```

## known issues

- Only supports queries from depth 0-2 currently.

## todo

- rename binary to btq (users can alias if they want at tq)

## why

- I couldn't get yq's experimental support for TOML working.
- I wanted a python implementation, all others seem to use go.

## links

- jq: https://github.com/stedolan/jq
- yq: https://github.com/kislyuk/yq
