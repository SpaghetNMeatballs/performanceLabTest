import sys
import os

if __name__ == '__main__':
    assert len(sys.argv) == 3, "Wrong amount of arguments passed"
    circle_path = sys.argv[1] if os.path.exists(sys.argv[1]) else os.getcwd()+'\\'+sys.argv[1]
    points_path = sys.argv[2] if os.path.exists(sys.argv[2]) else os.getcwd()+'\\'+sys.argv[2]
    if os.path.exists(circle_path):
        try:
            with open(circle_path, 'r') as circle:
                x, y = [int(i) for i in circle.readline().split()]
                radius = int(circle.readline())
        except TypeError:
            raise Exception("Wrong file structure")
    else:
        raise FileNotFoundError("File containing circle data not found")
    if os.path.exists(points_path):
        try:
            with open(points_path, 'r') as points:
                for point in points:
                    x1, y1 = [int(i) for i in point.split()]
                    result = (x - x1) ** 2 + (y - y1) ** 2
                    if result < radius ** 2:
                        print(1)
                    elif result == radius ** 2:
                        print(0)
                    else:
                        print(2)
        except TypeError:
            raise Exception("Wrong file structure")
    else:
        raise FileNotFoundError("File containing points data not found")
