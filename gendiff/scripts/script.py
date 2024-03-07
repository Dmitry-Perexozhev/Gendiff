#!/usr/bin/env python3
from gendiff.formaters.stylish import gen_stylish_format
from gendiff.formaters.plain import gen_plain_format
import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    if args.format == 'plain':
        print(gen_plain_format(args.first_file, args.second_file))
    else:
        print(gen_stylish_format(args.first_file, args.second_file))


def main():
    init_argparse()


if __name__ == '__main__':
    main()
