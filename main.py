"""Copy the entry.png sitting next to this script into the output directory.

The output directory is the value of the MAKEFUN_OUTPUT_DIR environment
variable when set and non-empty, otherwise /output. The file is copied
byte-identical under the same name, and the output directory is created if
it does not already exist. No network, randomness, or clock reads are used.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir():
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if value:
        return value
    return DEFAULT_OUTPUT_DIR


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), SOURCE_NAME)
    if not os.path.isfile(source):
        print("source not found: {0}".format(source), file=sys.stderr)
        return 1

    output_dir = resolve_output_dir()
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        print("cannot create output directory {0}: {1}".format(output_dir, exc), file=sys.stderr)
        return 1

    destination = os.path.join(output_dir, SOURCE_NAME)
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        print("cannot write {0}: {1}".format(destination, exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
