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
        "list_path", type=argparse.FileType("r"), help="List file"
    )
    list_path = sys.argv[1] if os.path.exists(sys.argv[1]) else os.getcwd() + '\\' + sys.argv[1]
    to_equalise = []
    with open(list_path, 'r') as list_file:
        for row in list_file:
            to_equalise.append(int(row))
    print(equalise_list(to_equalise))
