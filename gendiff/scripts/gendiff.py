import argparse

from gendiff.scripts.generate_diff import generate_difference
from gendiff.scripts.parser import parse_files


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()

    # first_file, second_file = parse_files(args.first_file, args.second_file)
    result = generate_difference(parse_files(args.first_file, args.second_file))
    print(result)

    
