import json
from gendiff.gendiff.generate_diff import generate_diff


def test_generate_diff_json():
    with open('tests/fixtures/tests_output.json') as output:
        data = json.load(output)
        stylish_file1_file2 = generate_diff('tests/fixtures/file1.json',
                                            'tests/fixtures/file2.json', 'stylish')
        assert stylish_file1_file2 == data['test_generate_diff_file1_file_2']
        stylish_file1_file2_recursive = generate_diff('tests/fixtures/file1_recursive.json',
                                                      'tests/fixtures/file2_recursive.json', 'stylish')
        assert stylish_file1_file2_recursive == data['test_stylish_format_file1_file2_recursive']
        plain_file1_file2_recursive = generate_diff('tests/fixtures/file1_recursive.json',
                                                    'tests/fixtures/file2_recursive.json', 'plain')
        assert plain_file1_file2_recursive == data['test_plain_format_file1_file2_recursive']


def test_generate_diff_yaml():
    with open('tests/fixtures/tests_output.json') as output:
        data = json.load(output)
        stylish_file1_file2 = generate_diff('tests/fixtures/file1.yaml',
                                            'tests/fixtures/file2.yaml', 'stylish')
        assert stylish_file1_file2 == data['test_generate_diff_file1_file_2']
        stylish_file1_file2_recursive = generate_diff('tests/fixtures/file1_recursive.yaml',
                                                      'tests/fixtures/file2_recursive.yaml', 'stylish')
        assert stylish_file1_file2_recursive == data['test_stylish_format_file1_file2_recursive']
        plain_file1_file2_recursive = generate_diff('tests/fixtures/file1_recursive.json',
                                                    'tests/fixtures/file2_recursive.json', 'plain')
        assert plain_file1_file2_recursive == data['test_plain_format_file1_file2_recursive']
