# tq

A barebones python tq (like jq, but for toml).

[![Build Status](https://travis-ci.com/aerickson/tq.svg?branch=master)](https://travis-ci.com/aerickson/tq)

## usage

```
./tq . test/test.toml
./tq .title test/test.toml
./tq .database.ports test/test.toml
```

## known issues

- Only supports queries from depth 0-2 currently. Patches accepted.
- No stdin support yet.

## why

- I couldn't get yq's experimental support for TOML working.
- I wanted a python implementation, all others seem to use go.

## links

- jq: https://github.com/stedolan/jq
- yq: https://github.com/kislyuk/yq
