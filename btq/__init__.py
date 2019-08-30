#!/usr/bin/env python3

import toml
import sys


def print_object(obj):
    if type(obj) == dict:
        print(toml.dumps(obj).strip())
    else:
        print(obj)


def main(file_path, toml_path):
    return_value = None
    if type(file_path) == str:
        data = toml.load(open(file_path))
    else:
        # this is a _io.TextIOWrapper object
        data = toml.loads(file_path.read())

    if toml_path == ".":
        print_object(data)
        return

    split_filter = toml_path.split(".")
    filter_length = len(split_filter)
    # print(split_filter)

    # TODO: how to support arbitrary depth without a ton of elif blocks?
    try:
        if filter_length == 2:
            return_value = data[split_filter[1]]
        elif filter_length == 3:
            return_value = data[split_filter[1]][split_filter[2]]
        else:
            print("ERROR: I don't know that query syntax yet (1).")
            sys.exit(1)
    except KeyError:
        print("ERROR: I don't know that query syntax yet (2).")
        sys.exit(1)

    print_object(return_value)
    sys.exit(0)
