import pytest
from gendiff.generate_diff import generate_diff
from gendiff.cli import format_diff


@pytest.fixture()
def first_file():
    return 'tests/fixtures/file1.json'


@pytest.fixture()
def second_file():
    return 'tests/fixtures/file2.json'


@pytest.fixture()
def expected_diff():
    with open('tests/fixtures/expected_diff.txt', 'r') as f:
        return f.read()


def test_gendiff(first_file, second_file, expected_diff):
    print(generate_diff(first_file, second_file))
    print(expected_diff)
    assert format_diff(generate_diff(first_file, second_file)) == expected_diff
