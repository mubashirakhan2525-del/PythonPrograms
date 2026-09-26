from importlib.machinery import SourceFileLoader

program = SourceFileLoader("largest_of_three", "Code/02_largest_of_three.py").load_module()


def test_largest_first():
    assert program.largest_of_three(10, 5, 3) == 10


def test_largest_second():
    assert program.largest_of_three(4, 12, 7) == 12


def test_largest_third():
    assert program.largest_of_three(2, 6, 15) == 15


def test_equal_numbers():
    assert program.largest_of_three(5, 5, 3) == 5


def test_negative_numbers():
    assert program.largest_of_three(-10, -3, -7) == -3


print("All test cases passed.")