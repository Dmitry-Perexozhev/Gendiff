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
    diffs = generate_diff(data_of_file1, data_of_file2)

    def recursive_stylish_format(dict_diffs, depth):
        result = []
        indent = REPLACER * (NUMBER_OF_INDENTS * depth - 2)
        for dif in dict_diffs:
            if 'status' in dif:
                if dif['status'] == 'unchanged':
                    result.append(f'{indent}  {dif["key"]}: {is_correct_output(dif["value"])}\n')
                elif dif['status'] == 'added':
                    if isinstance(dif['value'], dict):
                        result.append(f'{indent}+ {dif["key"]}: {{\n')
                        result += recursive_stylish_format(dif['value'], depth + 1)
                    else:
                        result.append(f'{indent}+ {dif["key"]}: {is_correct_output(dif["value"])}\n')
                elif dif['status'] == 'removed':
                    if isinstance(dif['value'], dict):
                        result.append(f'{indent}- {dif["key"]}: {{\n')
                        result += recursive_stylish_format(dif['value'], depth + 1)
                    else:
                        result.append(f'{indent}- {dif["key"]}: {is_correct_output(dif["value"])}\n')
                elif dif['status'] == 'has_children':
                    result.append(f'{indent}  {dif["key"]}: {{\n')
                    result += recursive_stylish_format(dif["value"], depth+1)
                elif dif['status'] == 'updated':
                    if isinstance(dif['old_value'], dict):
                        result.append(f'{indent}- {dif["key"]}: {{\n')
                        result += recursive_stylish_format(dif['old_value'], depth + 1)
                    else:
                        result.append(f'{indent}- {dif["key"]}: {is_correct_output(dif["old_value"])}\n')
                    if isinstance(dif['new_value'], dict):
                        result.append(f'{indent}+ {dif["key"]}: {{\n')
                        result += recursive_stylish_format(dif['new_value'], depth + 1)
                    else:
                        result.append(f'{indent}+ {dif["key"]}: {is_correct_output(dif["new_value"])}\n')
            else:
                if isinstance(dict_diffs[dif], dict):
                    result.append(f'{indent}  {dif}: {{\n')
                    result += recursive_stylish_format(dict_diffs[dif], depth + 1)
                else:
                    result.append(f'{indent}  {dif}: {is_correct_output(dict_diffs[dif])}\n')
        result.append(f'{indent[:-2]}}}\n')
        return result
    return '{\n'+''.join(recursive_stylish_format(diffs, 1))[:-1]


#print(gen_stylish_format('file1.json', 'file2.json'))

