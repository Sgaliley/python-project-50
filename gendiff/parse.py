import json
import yaml


def parse(data, format):
    if format.lower() == 'json':
        return json.loads(data)
    elif format.lower() in ('yaml', 'yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError('Unsupported data format')
