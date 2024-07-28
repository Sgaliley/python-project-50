#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def parse_args():
    string = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=string)
    parser.add_argument('first_file', help='what about first file')
    parser.add_argument('second_file', help='what about second file')
    parser.add_argument(
        "-f", "--format", default="stylish",
        choices=["stylish", "plain", "json"],
        help="output format, default: 'stylish'"
    )
    return parser.parse_args()


def main():
    """Запуск"""
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
