import sys
import os


def equalise_list(inp: list):
    m = sorted(inp)[len(inp) // 2]
    result = 0
    for i in inp:
        result+=abs(i-m)
    return result




if __name__ == '__main__':
    assert len(sys.argv) == 2, "Wrong amount of arguments passed"
    list_path = sys.argv[1] if os.path.exists(sys.argv[1]) else os.getcwd()+'\\'+sys.argv[1]
    to_equalise = []
    if os.path.exists(list_path):
        try:
            with open(list_path, 'r') as list_file:
                for row in list_file:
                    to_equalise.append(int(row))
        except TypeError:
            raise Exception("Wrong file structure")
    print(equalise_list(to_equalise))
