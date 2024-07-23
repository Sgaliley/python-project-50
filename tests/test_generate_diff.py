import pytest
from gendiff.generate_diff import generate_diff
from gendiff.parse import parse_file
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def test_generate_diff_stylish_12_json():
    data_1 = 'tests/fixtures/file1.json'
    data_2 = 'tests/fixtures/file2.json'
    expected_stylish_12 = open('tests/fixtures/test_stylish_12.txt').read()

    parsed_data1 = parse_file(data_1)
    parsed_data2 = parse_file(data_2)

    diff = generate_diff(parsed_data1, parsed_data2)
    formatted_diff = format_stylish(diff).strip()

    assert formatted_diff == expected_stylish_12


def test_generate_diff_stylish_12_yml():
    data_1 = 'tests/fixtures/file1.yml'
    data_2 = 'tests/fixtures/file2.yml'
    expected_stylish_12 = open('tests/fixtures/test_stylish_12.txt').read()

    parsed_data1 = parse_file(data_1)
    parsed_data2 = parse_file(data_2)

    diff = generate_diff(parsed_data1, parsed_data2)
    formatted_diff = format_stylish(diff).strip()

    assert formatted_diff == expected_stylish_12


def test_generate_diff_stylish_34():
    data_3 = 'tests/fixtures/file3.json'
    data_4 = 'tests/fixtures/file4.json'
    expected_stylish_34 = open('tests/fixtures/test_stylish_34.txt').read()

    parsed_data3 = parse_file(data_3)
    parsed_data4 = parse_file(data_4)

    diff = generate_diff(parsed_data3, parsed_data4)
    formatted_diff = format_stylish(diff).strip()

    assert formatted_diff == expected_stylish_34


def test_generate_diff_stylish_34_yml():
    data_3 = 'tests/fixtures/file3.yml'
    data_4 = 'tests/fixtures/file4.yml'
    expected_stylish_34 = open('tests/fixtures/test_stylish_34.txt').read()

    parsed_data3 = parse_file(data_3)
    parsed_data4 = parse_file(data_4)

    diff = generate_diff(parsed_data3, parsed_data4)
    formatted_diff = format_stylish(diff).strip()

    assert formatted_diff == expected_stylish_34


def test_generate_diff_plain_34():
    data_3 = 'tests/fixtures/file3.json'
    data_4 = 'tests/fixtures/file4.json'
    expected_plain_34 = open('tests/fixtures/test_plain_34.txt').read()

    parsed_data3 = parse_file(data_3)
    parsed_data4 = parse_file(data_4)

    diff = generate_diff(parsed_data3, parsed_data4)
    formatted_diff = format_plain(diff).strip()

    assert formatted_diff == expected_plain_34


def test_generate_diff_json_34():
    data_3 = 'tests/fixtures/file3.json'
    data_4 = 'tests/fixtures/file4.json'
    expected_json_34 = open('tests/fixtures/test_json_34.txt').read()

    parsed_data3 = parse_file(data_3)
    parsed_data4 = parse_file(data_4)

    diff = generate_diff(parsed_data3, parsed_data4)
    formatted_diff = format_json(diff).strip()

    assert formatted_diff == expected_json_34
