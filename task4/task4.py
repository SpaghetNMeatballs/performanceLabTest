import argparse
from typing import TextIO



def process_list_file(list_file: TextIO) -> list:
    to_equalise = []
    for row in list_file:
        try:
            to_equalise.append(int(row))
        except TypeError:
            print(f"ERROR! Invalid row in list file: {row}")
    return to_equalise


def equalise_list(inp: list):
    m = sorted(inp)[len(inp) // 2]
    result = 0
    for i in inp:
        result += abs(i - m)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("list_file", type=argparse.FileType("r"), help="List file")
    args = parser.parse_args()
    list_file = args.list_file
    to_equalise = process_list_file(list_file)
    print(equalise_list(to_equalise))


if __name__ == "__main__":
    main()
