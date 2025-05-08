import sys
import argparse


def calc_path(n, m):
    result = ''
    last_node = 0
    while True:
        result += str(last_node + 1)
        last_node += m - 1
        last_node %= n
        if last_node == 0:
            break
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "n", type=int, help="List length"
    )
    parser.add_argument(
        "m", type=int, help="Cycle length"
    )
    args = parser.parse_args()
    n, m = args.n, args.m
    print(calc_path(n, m))
