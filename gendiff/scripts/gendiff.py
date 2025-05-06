import argparse

from .generate_diff import generate_diff
from .parser import parse_files


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", "--format", help="set format of output", choices=[
        "plain", "stylish", "json"], default="stylish")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()

    first_file, second_file = parse_files(args.first_file, args.second_file)
    result = generate_diff(first_file, second_file, args.format)
    print(result)
