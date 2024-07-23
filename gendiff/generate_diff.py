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


def make_diff(data1, data2):
    diff = {}
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    keys_union = sorted(keys1.union(keys2))
    for key in keys_union:
        if key in data1 and key not in keys2:
            diff[key] = {'operation': 'removed', 'old': data1[key]}
        elif key not in keys1 and key in keys2:
            diff[key] = {'operation': 'add', 'new': data2[key]}
        else:
            if data1[key] == data2[key]:
                diff[key] = {'operation': 'same', 'value': data1[key]}
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[key] = {
                    'operation': 'nested',
                    'value': make_diff(data1[key], data2[key]),
                }
            else:
                diff[key] = {
                    'operation': 'changed',
                    'old': data1[key],
                    'new': data2[key],
                }
    return diff


def generate_diff(first_file, second_file, formatter='stylish'):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)
    diff = make_diff(data1, data2)
    return format_diff(diff, formatter)
