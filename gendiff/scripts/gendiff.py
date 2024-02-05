#!/usr/bin/env python3
import json
import yaml
import argparse


def generate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1) as file1, open(path_to_file2) as file2:
        if path_to_file1.split('.')[1] == 'json':
            data1 = json.load(file1)
            data2 = json.load(file2)
        elif path_to_file1.split('.')[1] == 'yaml':
            data1 = yaml.load(file1, Loader=yaml.FullLoader)
            data2 = yaml.load(file2, Loader=yaml.FullLoader)
        keys = sorted(set(data1.keys()) | set(data2.keys()))
        dif_stroke = ''
        for key in keys:
            if key in data1 and key in data2:
                if data1.get(key) == data2.get(key):
                    dif_stroke += f'  {key}: {data1.get(key)}\n'
                else:
                    dif_stroke += f'- {key}: {data1.get(key)}\n'
                    dif_stroke += f'+ {key}: {data2.get(key)}\n'
            elif key in data1:
                dif_stroke += f'- {key}: {data1.get(key)}\n'
            else:
                dif_stroke += f'+ {key}: {data2.get(key)}\n'
        return dif_stroke


def init_argparse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    print('{')
    for stroke in generate_diff(args.first_file,
                                args.second_file).split('\n')[:-1]:
        print('  ', stroke)
    print('}')


def main():
    init_argparse()


if __name__ == '__main__':
    main()
