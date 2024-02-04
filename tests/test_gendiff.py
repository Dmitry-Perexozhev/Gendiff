#!/usr/bin/env python3
#from gendiff.scripts.gendiff_json import generate_diff
import json


def generate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1) as file1, open(path_to_file2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        keys = sorted(set(data1.keys()) | set(data2.keys()))
        dif_stroke = ''
        for key in keys:
            if key in data1 and key in data2:
                if data1.get(key) == data2.get(key):
                    dif_stroke += f'  {key}: {data1.get(key)}\n'
                else:
                    dif_stroke += f'- {key}: {data1.get(key)}\n'
                    dif_stroke += f'+ {key}: {data2.get(key)}\n'
            elif key in data1:
                dif_stroke += f'- {key}: {data1.get(key)}\n'
            else:
                dif_stroke += f'+ {key}: {data2.get(key)}\n'
        return dif_stroke

def test_generate_diff():
    with open('fixtures/tests_output.json') as output:
        data = json.load(output)
        result_compare_file1_file2 = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
        assert result_compare_file1_file2 == data['test_generate_diff_file1_file_2']
        result_compare_file3_file4 = generate_diff('fixtures/file3.json', 'fixtures/file4.json')
        assert result_compare_file3_file4 == data['test_generate_diff_file3_file_4']


