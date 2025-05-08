from task4 import equalise_list

def test_default_list():
    assert equalise_list([1,10,2,9]) == 16

def test_odd_list():
    assert equalise_list([9,9,9,10,10]) == 2

def test_even_list():
    assert equalise_list([9,10,10,10]) == 1