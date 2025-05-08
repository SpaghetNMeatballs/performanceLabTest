import pytest

from task2 import Circle, Point, check_point, Placement

@pytest.fixture
def my_circle():
    return Circle(1, 1, 5)

@pytest.fixture
def point_inside():
    return Point(0,0)

@pytest.fixture
def point_border():
    return Point(1, 6)

@pytest.fixture
def point_outer():
    return Point(6, 6)

def test_points(point_outer, point_border, point_inside, my_circle):
    assert check_point(point_outer, my_circle) is Placement.OUTSIDE
    assert check_point(point_border, my_circle) is Placement.BORDER
    assert check_point(point_inside, my_circle) is Placement.INSIDE