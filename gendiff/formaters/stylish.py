from gendiff.gendiff.gendiff import generate_diff
from gendiff.loader.loader import load_file

def gen_stylish_format(path_to_file1, path_to_file2):
    data_of_file1, data_of_file2 = load_file(path_to_file1, path_to_file2)  # загрузка данных из файлов
    dif_stroke = ''
    dif_stroke += '{\n'
    keys = sorted(set(data_of_file1.keys()) | set(data_of_file2.keys()))
    for key in keys:
        dif = generate_diff(key, data_of_file1.get(key), data_of_file2.get(key))
        if dif['status'] == 'unchanged':
            dif_stroke += f'  {key}: {dif["old_value"]}\n'
        elif dif['status'] == 'added':
            dif_stroke += f'+ {key}: {dif["new_value"]}\n'
        elif dif['status'] == 'removed':
            dif_stroke += f'- {key}: {dif["old_value"]}\n'
        else:
            dif_stroke += f'- {key}: {dif["old_value"]}\n'
            dif_stroke += f'+ {key}: {dif["new_value"]}\n'
    dif_stroke += '}'
    return dif_stroke
