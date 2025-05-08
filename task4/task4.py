import sys
import os
import argparse


def equalise_list(inp: list):
    m = sorted(inp)[len(inp) // 2]
    result = 0
    for i in inp:
        result += abs(i - m)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "list_file", type=argparse.FileType("r"), help="List file"
    )
    args = parser.parse_args()
    list_file = args.list_file
    to_equalise = []
    for row in list_file:
        to_equalise.append(int(row))
    print(equalise_list(to_equalise))
