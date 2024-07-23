import yaml
import json
from pathlib import Path


def parse_file(file_path):
    file_path = Path(file_path)

    if file_path.suffix.lower() in ('.json',):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.suffix.lower() in ('.yaml', '.yml'):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise ValueError('Unsupported file format')
