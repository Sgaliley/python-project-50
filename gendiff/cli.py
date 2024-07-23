import argparse
import pathlib
from gendiff.generate_diff import generate_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.parse import parse_file


def format_diff(diff, formatter='stylish'):
    formatters = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json,
    }
    return formatters[formatter](diff)


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output',
    )
    args = parser.parse_args()

    f1 = args.first_file
    f2 = args.second_file
    formatter = args.format
    diff = generate_diff(parse_file(f1), parse_file(f2))
    return format_diff(diff, formatter)
