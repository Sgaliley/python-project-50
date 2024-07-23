def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def build_path(path, key):
    return f'{path}.{key}' if path else key


def format_plain(diff, path=''):
    lines = []
    for key, info in diff.items():
        full_key = f'{path}{key}' if path else key
        operation = info['operation']
        if operation == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif operation == 'add':
            lines.append(
                f"Property '{full_key}' was added with value: {format_value(info['new'])}"
            )
        elif operation == 'changed':
            old_value = format_value(info['old'])
            new_value = format_value(info['new'])
            lines.append(
                f"Property '{full_key}' was updated. From {old_value} to {new_value}"
            )
        elif operation == 'nested':
            nested_lines = format_plain(info['value'], f'{full_key}.')
            lines.append(nested_lines)
    return '\n'.join(lines)
