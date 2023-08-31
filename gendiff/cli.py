import argparse


def parser(argv=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output',)
    return parser.parse_args(argv)
