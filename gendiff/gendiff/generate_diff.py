from gendiff.gendiff.build_diff import build_diff
from gendiff.loader.loader import load_file
from gendiff.formaters import stylish, plain, to_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    try:
        data_of_file1, data_of_file2 = load_file(file_path1, file_path2)
    except ValueError:
        return 'Wrong paths'
    diffs = build_diff(data_of_file1, data_of_file2)
    if format_name == 'plain':
        result = plain.gen_plain_format(diffs, [])
        result = '\n'.join(result)
    elif format_name == 'json':
        result = to_json.gen_json_format(diffs)
    else:
        result = stylish.gen_stylish_format(diffs, 1)
        result = '\n'.join(result)
    return result
