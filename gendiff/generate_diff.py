import json


def generate_diff(file1, file2):
    with (
        open(file1, 'r') as f1,
        open(file2, 'r') as f2,
    ):
        data1 = json.load(f1)
        data2 = json.load(f2)
        diff = {}

        keys_union = set(data1.keys()).union(set(data2.keys()))

        for key in sorted(keys_union):
            if key in data1 and key not in data2:
                diff[f'- {key}'] = data1[key]
            elif key in data2 and key not in data1:
                diff[f'+ {key}'] = data2[key]
            elif data1[key] != data2[key]:
                diff[f'- {key}'] = data1[key]
                diff[f'+ {key}'] = data2[key]
            else:
                diff[f'  {key}'] = data1[key]

        return diff
