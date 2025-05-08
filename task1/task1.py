import sys


def calc_path(n, m):
    result = ''
    last_node = 0
    while True:
        result += str(last_node+1)
        last_node += m - 1
        last_node %= n
        if last_node == 0:
            break
    return result


if __name__ == '__main__':
    assert len(sys.argv) == 3, "Wrong amount of arguments passed"
    n, m = (int(i) for i in sys.argv[1:])
    print(calc_path(n, m))
