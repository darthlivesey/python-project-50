import argparse
from gendiff.scripts.generate_diff import generate_difference


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", "--format", help = "set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()

    print(generate_difference(args.first_file, args.second_file))

    
