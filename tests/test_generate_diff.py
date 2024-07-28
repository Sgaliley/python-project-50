import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    'file1,file2,form,expected',
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish", 'tests/fixtures/test_stylish_12.txt'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "plain", 'tests/fixtures/test_plain_12.txt'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "json", 'tests/fixtures/test_json_12.txt'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/test_stylish_12.txt'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "plain", 'tests/fixtures/test_plain_12.txt'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "json", 'tests/fixtures/test_json_12.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', "stylish", 'tests/fixtures/test_stylish_34.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', "plain", 'tests/fixtures/test_plain_34.txt'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', "json", 'tests/fixtures/test_json_34.txt'),
        ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/test_stylish_34.txt'),
        ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml', "plain", 'tests/fixtures/test_plain_34.txt'),
        ('tests/fixtures/file3.yml', 'tests/fixtures/file4.yml', "json", 'tests/fixtures/test_json_34.txt'),
    ]
)
def test_generate_diff(file1, file2, form, expected):
    with open(expected, 'r') as f:
        expected_content = f.read().rstrip()
    assert generate_diff(file1, file2, form) == expected_content
