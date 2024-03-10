#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli.argparse import init_argparse


def main():
    file_path1, file_path2, format_name = init_argparse()
    print(generate_diff(file_path1, file_path2, format_name))


if __name__ == '__main__':
    main()
