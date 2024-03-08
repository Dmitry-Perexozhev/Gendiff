from gendiff.gendiff.gendiff import generate_diff
from gendiff.loader.loader import load_file


def is_correct_output(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    elif isinstance(obj, dict):
        return '[complex value]'
    return "\'"+obj+"\'"


def gen_plain_format(path_to_file1, path_to_file2):
    data_of_file1, data_of_file2 = load_file(path_to_file1, path_to_file2)  # загрузка данных из файлов
    diffs = generate_diff(data_of_file1, data_of_file2)

    def recursive_plain_format(dict_diffs, path):
        result = []
        for dif in dict_diffs:
            if dif['status'] == 'has_children':
                result += recursive_plain_format(dif["value"], path+[dif["key"]])
            elif dif['status'] == 'added':
                result.append(f'Property \'{".".join(path+[dif["key"]])}\' was added with value: {is_correct_output(dif["value"])}')
            elif dif['status'] == 'removed':
                result.append(f'Property \'{".".join(path+[dif["key"]])}\' was removed')
            elif dif['status'] == 'updated':
                result.append(f'Property \'{".".join(path+[dif["key"]])}\' was updated. From {is_correct_output(dif["old_value"])} to {is_correct_output(dif["new_value"])}')
        return result
    return '\n'.join(recursive_plain_format(diffs, []))
#print(gen_plain_format('file1_recursive.json', 'file2_recursive.json'))
