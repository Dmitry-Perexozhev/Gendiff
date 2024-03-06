from gendiff.gendiff.gendiff import generate_diff
from gendiff.loader.loader import load_file

NUMBER_OF_INDENTS = 4
REPLACER = ' '


def is_correct_output(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    return obj


def gen_stylish_format(path_to_file1, path_to_file2):
    data_of_file1, data_of_file2 = load_file(path_to_file1, path_to_file2)  # загрузка данных из файлов
    dif_stroke = '{\n'
    diffs = generate_diff(data_of_file1, data_of_file2)

    def recursive_stylish_format(dict_diffs, depth):
        nonlocal dif_stroke
        indent = REPLACER * (NUMBER_OF_INDENTS * depth - 2)
        for dif in dict_diffs:
            if 'status' in dif:
                if dif['status'] == 'unchanged':
                    dif_stroke += f'{indent}  {dif["key"]}: {is_correct_output(dif["value"])}\n'
                elif dif['status'] == 'added':
                    if isinstance(dif['value'], dict):
                        dif_stroke += f'{indent}+ {dif["key"]}: {{\n'
                        recursive_stylish_format(dif['value'], depth + 1)
                    else:
                        dif_stroke += f'{indent}+ {dif["key"]}: {is_correct_output(dif["value"])}\n'
                elif dif['status'] == 'removed':
                    if isinstance(dif['value'], dict):
                        dif_stroke += f'{indent}- {dif["key"]}: {{\n'
                        recursive_stylish_format(dif['value'], depth + 1)
                    else:
                        dif_stroke += f'{indent}- {dif["key"]}: {is_correct_output(dif["value"])}\n'
                elif dif['status'] == 'has_children':
                    dif_stroke += f'{indent}  {dif["key"]}: {{\n'
                    recursive_stylish_format(dif["value"], depth+1)
                elif dif['status'] == 'updated':
                    if isinstance(dif['old_value'], dict):
                        dif_stroke += f'{indent}- {dif["key"]}: {{\n'
                        recursive_stylish_format(dif['old_value'], depth + 1)
                    else:
                        dif_stroke += f'{indent}- {dif["key"]}: {is_correct_output(dif["old_value"])}\n'
                    if isinstance(dif['new_value'], dict):
                        dif_stroke += f'{indent}+ {dif["key"]}: {{\n'
                        recursive_stylish_format(dif['new_value'], depth + 1)
                    else:
                        dif_stroke += f'{indent}+ {dif["key"]}: {is_correct_output(dif["new_value"])}\n'
            else:
                if isinstance(dict_diffs[dif], dict):
                    dif_stroke += f'{indent}  {dif}: {{\n'
                    recursive_stylish_format(dict_diffs[dif], depth + 1)
                else:
                    dif_stroke += f'{indent}  {dif}: {is_correct_output(dict_diffs[dif])}\n'
        dif_stroke += f'{indent[:-2]}}}\n'
    recursive_stylish_format(diffs, 1)
    dif_stroke = dif_stroke[:-2] + '}'

    return dif_stroke

