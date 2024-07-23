def format_value(value, indent):
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(
                f"{indent}    {k}: {format_value(v, indent + '    ')}"
            )
        lines.append(indent + '}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return 'false' if not value else 'true'
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_stylish(data, indent=''):
    diff = ['{']
    for key, info in data.items():
        operation = info['operation']
        if operation == 'removed':
            diff.append(
                f"{indent}  - {key}: {format_value(info['old'], indent + '    ')}"
            )
        elif operation == 'add':
            diff.append(
                f"{indent}  + {key}: {format_value(info['new'], indent + '    ')}"
            )
        elif operation == 'same':
            diff.append(
                f"{indent}    {key}: {format_value(info['value'], indent + '    ')}"
            )
        elif operation == 'changed':
            diff.append(
                f"{indent}  - {key}: {format_value(info['old'], indent + '    ')}"
            )
            diff.append(
                f"{indent}  + {key}: {format_value(info['new'], indent + '    ')}"
            )
        elif operation == 'nested':
            nested_diff = format_stylish(info['value'], indent + '    ')
            diff.append(f'{indent}    {key}: {nested_diff}')
    diff.append(indent + '}')
    return '\n'.join(diff)
