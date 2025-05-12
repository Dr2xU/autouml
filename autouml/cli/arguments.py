import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Generate UML class diagrams from Python project structure.'
    )

    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to the Python project directory (default: current directory)'
    )

    parser.add_argument(
        '--output', '-o',
        metavar='OUTPUT',
        required=False,
        default='diagram.png',
        help='Output PNG file name (default: diagram.png)'
    )

    args = parser.parse_args()
    return os.path.abspath(args.path), os.path.abspath(args.output)
