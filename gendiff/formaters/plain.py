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
    dif_stroke = ''

    def recursive_plain_format(dict_diffs, path):
        nonlocal dif_stroke
        for dif in dict_diffs:
            if dif['status'] == 'has_children':
                recursive_plain_format(dif["value"], path+[dif["key"]])
            elif dif['status'] == 'added':
                dif_stroke += f'Property \'{".".join(path+[dif["key"]])}\' was added with value: {is_correct_output(dif["value"])}\n'
            elif dif['status'] == 'removed':
                dif_stroke += f'Property \'{".".join(path+[dif["key"]])}\' was removed\n'
            elif dif['status'] == 'updated':
                dif_stroke += f'Property \'{".".join(path+[dif["key"]])}\' was updated. From {is_correct_output(dif["old_value"])} to {is_correct_output(dif["new_value"])}\n'
    recursive_plain_format(diffs, [])
    return dif_stroke[:-1]

