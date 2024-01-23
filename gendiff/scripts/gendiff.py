#!/usr/bin/env python3
import json
import argparse

def generate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1) as file1, open(path_to_file2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        keys = sorted(set(data1.keys()) | set(data2.keys()))
        print('{')
        for key in keys:
            if key in data1 and key in data2:
                if data1.get(key) == data2.get(key):
                    print(f'    {key}: {data1.get(key)}')
                else:
                    print(f'  - {key}: {data1.get(key)}')
                    print(f'  + {key}: {data2.get(key)}')
            elif key in data1:
                print(f'  - {key}: {data1.get(key)}')
            else:
                print(f'  + {key}: {data2.get(key)}')
        print('}')

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)



if __name__ == '__main__':
    main()