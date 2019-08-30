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

    split_filter = toml_path.split(".")
    # drop the first .
    split_filter = split_filter[1:]
    # print(split_filter)

    # set the return value to whole data object and refine gradually
    # based on the filter in for loop below.
    return_value = data
    try:
        for item in split_filter:
            # if item is '', . was passed in
            # TODO: this allows trailing dots vs just the simple
            # '.' filter input. is that legal syntax?
            if item == '':
                break
            elif item.endswith(']'):
                array_parts = item.split('[')
                filter_key = array_parts[0]
                filter_index = int(array_parts[1][:-1])
                return_value = return_value[filter_key][filter_index]
            else:
                return_value = return_value[item]
    except KeyError:
        print("ERROR: Invalid key ('%s')!" % item)
        sys.exit(1)
    except IndexError:
        print("ERROR: Array index is invalid ('%s')!" % item)
        sys.exit(1)
    except ValueError:
        print("ERROR: Malformed array filter ('%s')!" % item)
        sys.exit(1)

    print_object(return_value)
    sys.exit(0)
