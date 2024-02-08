import json
import yaml


def load_file(path_to_file1, path_to_file2):
    with open(path_to_file1) as file1, open(path_to_file2) as file2:
        if path_to_file1.endswith('.json'):
            data_of_file1 = json.load(file1)
            data_of_file2 = json.load(file2)
        else:
            data_of_file1 = yaml.load(file1, Loader=yaml.FullLoader)
            data_of_file2 = yaml.load(file2, Loader=yaml.FullLoader)
    return data_of_file1, data_of_file2
