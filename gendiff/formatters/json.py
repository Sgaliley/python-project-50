import json


def format_json(diff):
    json_result = json.dumps(diff, indent=4)
    return json_result
