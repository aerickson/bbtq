#!/usr/bin/env python3

import sys

import toml


class BTQException(Exception):
    def __init__(self, message):
        self.message = message


def print_object(obj):
    if type(obj) == dict:
        print(toml.dumps(obj).strip())
    else:
        print(obj)

def aaa(string):
    return string


def filter_toml(toml_object, filter_str):
    split_filter = filter_str.split(".")
    # drop the first .
    split_filter = split_filter[1:]
    # print(split_filter)

    # set the return value to whole data object and refine gradually
    # based on the filter in for loop below.
    return_value = toml_object
    try:
        for item in split_filter:
            # if item is '', . was passed in
            # TODO: this allows trailing dots vs just the simple
            # '.' filter input. is that legal syntax?
            if item == "":
                break
            elif item.endswith("]"):
                array_parts = item.split("[")
                filter_key = array_parts[0]
                filter_index = int(array_parts[1][:-1])
                return_value = return_value[filter_key][filter_index]
            else:
                return_value = return_value[item]
    except KeyError:
        raise BTQException("ERROR: Invalid key ('%s')!" % item)
    except IndexError:
        raise BTQException("ERROR: Array index is invalid ('%s')!" % item)
    except ValueError:
        raise BTQException("ERROR: Malformed array filter ('%s')!" % item)
    return return_value


def main(file_path, toml_path):
    return_value = None
    if type(file_path) == str:
        data = toml.load(open(file_path))
    else:
        # this is a _io.TextIOWrapper object
        data = toml.loads(file_path.read())

    try:
        return_value = filter_toml(data, toml_path)
    except BTQException as e:
        print(e.message)
        sys.exit(1)

    print_object(return_value)
    sys.exit(0)
