import argparse
import math
from dataclasses import dataclass
from enum import IntEnum
from typing import Generator, TextIO


class Placement(IntEnum):
    INSIDE = 1
    BORDER = 0
    OUTSIDE = 2


@dataclass
class Circle:
    x: float
    y: float
    r: float


@dataclass
class Point:
    x: float
    y: float


def read_circle_data(f: TextIO) -> Circle:
    try:
        x, y = (float(i) for i in f.readline().split(" "))
    except ValueError:
        print("ERROR! Invalid circle center coordinates!")
        exit(1)
    try:
        radius = float(f.readline())
    except ValueError:
        print("ERROR! Invalid radius!")
        exit(1)
    return Circle(x=x, y=y, r=radius)


def read_points(f: TextIO) -> list:
    result = []
    for row in f:
        try:
            x, y = (float(i) for i in row.split())
        except ValueError:
            print("ERROR! Invalid point coordinates")
            exit(1)
        result.append(Point(x, y))
    return result


def check_point(point: Point, circle: Circle) -> Placement:
    x = point.x - circle.x
    y = point.y - circle.y
    distance = math.sqrt(x * x + y * y)
    if math.isclose(circle.r, distance):
        return Placement.BORDER
    if circle.r > distance:
        return Placement.INSIDE
    return Placement.OUTSIDE


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "circle", type=argparse.FileType("r"), help="circle coordinates"
    )
    parser.add_argument(
        "points", type=argparse.FileType("r"), help="points coordinates"
    )
    args = parser.parse_args()
    circle = read_circle_data(args.circle)
    for point in read_points(args.points):
        print(check_point(circle=circle, point=point))


if __name__ == "__main__":
    main()
