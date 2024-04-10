import os
from bids_validator import BIDSValidator
from argparse import ArgumentParser
from pathlib import Path


def parse_args():
    parser = ArgumentParser(
        description=(
            "Recursively check each file in a root "
            "directory for BIDS compliance."
        )
    )
    parser.add_argument(
        "root", help="Root directory of the BIDS dataset.", type=Path
    )
    return parser.parse_args()


def main():
    """Traverse a directory and print all non-bids compliant file paths."""
    args = parse_args()
    len_root = len(str(args.root))
    print(len_root)
    validator = BIDSValidator()
    for dir_path, dir_names, file_names in os.walk(args.root):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            formatted_path = file_path[len_root:]
            if not validator.is_bids(formatted_path):
                print(file_path)


if __name__ == "__main__":
    main()
