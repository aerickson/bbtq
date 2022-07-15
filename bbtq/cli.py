import argparse
import sys

from . import __version__, package_name
from . import core


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        type=argparse.FileType("r"),
        default=None if sys.stdin.isatty() else sys.stdin,
        help='accepts "-" (stdin) also',
    )
    parser.add_argument(
        "filter",
        nargs="?",
        default=".",
        help='defaults to "." (shows the entire document)',
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{package_name} {__version__}, barebones TOML query",
    )
    args = parser.parse_args()

    core.main(args.file, args.filter)


if __name__ == "__main__":
    main()
