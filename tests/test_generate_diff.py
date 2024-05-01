import pytest
from gendiff.generate_diff import generate_diff
from gendiff.cli import format_diff


@pytest.fixture()
def first_file_json():
    return 'tests/fixtures/file1.json'


@pytest.fixture()
def first_file_yaml():
    return 'tests/fixtures/file1.yml'

@pytest.fixture()
def second_file_json():
    return 'tests/fixtures/file2.json'


@pytest.fixture()
def second_file_yaml():
    return 'tests/fixtures/file2.yml'

@pytest.fixture()
def expected_diff():
    with open('tests/fixtures/expected_diff_json.txt', 'r') as f:
        return f.read()


def test_gendiff_json(first_file_json, second_file_json, expected_diff):
    assert format_diff(generate_diff(first_file_json, second_file_json)) == expected_diff

def test_gendiff_yaml(first_file_yaml, second_file_yaml, expected_diff):
    assert format_diff(generate_diff(first_file_yaml, second_file_yaml)) == expected_diff
