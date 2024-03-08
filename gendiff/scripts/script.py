#!/usr/bin/env python3
from gendiff.gendiff.generate_diff import generate_diff
import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    return [args.first_file, args.second_file, args.format]


def main():
    file_path1, file_path2, format_name = init_argparse()
    print(generate_diff(file_path1, file_path2, format_name))


if __name__ == '__main__':
    main()
