import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,form,expected',
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish", 'tests/fixtures/test_stylish_12.txt'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/test_stylish_12.txt'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/test_stylish_12.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/test_stylish_34.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/test_stylish_34.txt'),
        ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/test_stylish_34.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "plain", 'tests/fixtures/test_plain_34.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "json", 'tests/fixtures/test_json_34.txt')],
)
def test_generate_diff(file1, file2, form, expected):
    assert generate_diff(file1, file2, form) == open(expected).read().rstrip()
