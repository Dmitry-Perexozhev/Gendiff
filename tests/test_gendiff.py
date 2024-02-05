#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
import pytest
import json
import yaml


def test_generate_diff():
    with open('tests/fixtures/tests_output.json') as output:
        data = json.load(output)
        result_compare_file1_file2 = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
        assert result_compare_file1_file2 == data['test_generate_diff_file1_file_2']
        result_compare_file3_file4 = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json')
        assert result_compare_file3_file4 == data['test_generate_diff_file3_file_4']

def test_generate_diff_yaml():
    with open('tests/fixtures/tests_output.json') as output:
        data = json.load(output)
        result_compare_file1_file2 = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
        print(result_compare_file1_file2)
        assert result_compare_file1_file2 == data['test_generate_diff_file1_file_2']


