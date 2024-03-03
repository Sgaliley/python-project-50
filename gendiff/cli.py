import argparse
import pathlib
from gendiff.generate_diff import generate_diff


def format_diff(diff):
    formatted_diff = ['{']
    for key, value in diff.items():
        formatted_diff.append(f'  {key}: {value}')
    formatted_diff.append('}')
    return '\n'.join(formatted_diff)


def gendiff():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=pathlib.Path)
    parser.add_argument("second_file", type=pathlib.Path)
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    f1 = args.first_file
    f2 = args.second_file
    diff = generate_diff(f1, f2)
    print(format_diff(diff))
