import json
from pathlib import Path

import yaml


def parse_files(first_filepath, second_filepath):
    if Path(first_filepath).suffix == ".json":
        first_file = json.load(open(first_filepath))
    elif (Path(first_filepath).suffix == ".yaml" or
          Path(first_filepath).suffix == ".yml"):
        first_file = yaml.safe_load(open(first_filepath))

    if Path(second_filepath).suffix == ".json":
        second_file = json.load(open(second_filepath))
    elif (Path(second_filepath).suffix == ".yaml" or
          Path(second_filepath).suffix == ".yml"):
        second_file = yaml.safe_load(open(second_filepath))

    return first_file, second_file


# def first_file_parse(first_filepath):
#     if Path(first_filepath).suffix == ".json":
#         first_file = json.load(open(first_filepath))
#     elif (Path(first_filepath).suffix == ".yaml" or
#           Path(first_filepath).suffix == ".yml"):
#         first_file = yaml.safe_load(open(first_filepath))

#     return first_file


# def second_file_parse(second_filepath):
#     if Path(second_filepath).suffix == ".json":
#         second_file = json.load(open(second_filepath))
#     elif (Path(second_filepath).suffix == ".yaml" or
#           Path(second_filepath).suffix == ".yml"):
#         second_file = yaml.safe_load(open(second_filepath))