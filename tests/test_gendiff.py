#!/usr/bin/env python3
from gendiff.formaters.stylish import gen_stylish_format
from gendiff.formaters.plain import gen_plain_format
import json


def test_generate_diff_json():
    with open('tests/fixtures/tests_output.json') as output:
        data = json.load(output)
        result_compare_file1_file2 = gen_stylish_format('tests/fixtures/file1.json',
                                                        'tests/fixtures/file2.json')
        assert result_compare_file1_file2 == data['test_generate_diff_file1_file_2']
        result_compare_file3_file4 = gen_stylish_format('tests/fixtures/file3.json',
                                                        'tests/fixtures/file4.json')
        assert result_compare_file3_file4 == data['test_generate_diff_file3_file_4']
        result_stylish_compare_file1_file2_recursive = gen_stylish_format('tests/fixtures/file1_recursive.json',
                                                                          'tests/fixtures/file2_recursive.json')
        assert result_stylish_compare_file1_file2_recursive == data['test_stylish_format_file1_file2_recursive']
        result_plain_compare_file1_file2_recursive = gen_plain_format('tests/fixtures/file1_recursive.json',
                                                                      'tests/fixtures/file2_recursive.json')
        assert result_plain_compare_file1_file2_recursive == data['test_plain_format_file1_file2_recursive']


def test_generate_diff_yaml():
    with open('tests/fixtures/tests_output.json') as output:
        data = json.load(output)
        result_compare_file1_file2 = gen_stylish_format('tests/fixtures/file1.yaml',
                                                        'tests/fixtures/file2.yaml')
        assert result_compare_file1_file2 == data['test_generate_diff_file1_file_2']
        result_compare_file1_file2_recursive = gen_stylish_format('tests/fixtures/file1_recursive.yaml',
                                                                  'tests/fixtures/file2_recursive.yaml')
        assert result_compare_file1_file2_recursive == data['test_stylish_format_file1_file2_recursive']

