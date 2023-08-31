from gendiff.cli import parser
from gendiff.generate_diff import generate_diff
import sys


def main(argv=None):
    args = parser(argv)
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main(sys.argv[1:])
