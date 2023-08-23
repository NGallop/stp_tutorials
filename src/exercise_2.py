import argparse

parser = argparse.ArgumentParser(
    description='')
parser.add_argument(
    '-i', '--input', required = True, help='Input file')
parser.add_argument(
    '-o', '--output', required=True, help='Output file')
parser.add_argument(
    '-e', '--example_1', action='store_true', help='')
parser.add_argument(
    '-f', '--example_2', action='store_true', help='')

args = parser.parse_args()
