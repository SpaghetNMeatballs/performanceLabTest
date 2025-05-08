from task1 import calc_path


def test_example1():
    assert calc_path(4, 3) == "13"


def test_example2():
    assert calc_path(5, 4) == "14253"
