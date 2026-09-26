from importlib.machinery import SourceFileLoader

program = SourceFileLoader("second_largest", "Code/15_second_largest.py").load_module()


def test_second_largest():
    assert program.second_largest([10, 20, 5, 8]) == 10


def test_second_largest_unsorted():
    assert program.second_largest([4, 9, 2, 7, 5]) == 7


def test_second_largest_with_duplicates():
    assert program.second_largest([10, 10, 8, 5]) == 8


def test_negative_numbers():
    assert program.second_largest([-10, -5, -8, -2]) == -5


def test_simple_list():
    assert program.second_largest([1, 2]) == 1


print("All test cases passed.")