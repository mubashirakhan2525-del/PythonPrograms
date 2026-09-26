from importlib.machinery import SourceFileLoader

program = SourceFileLoader("missing_number", "Code/18_missing_number.py").load_module()


def test_missing_number():
    assert program.find_missing_number([1, 2, 3, 5]) == 4


def test_missing_first_number():
    assert program.find_missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert program.find_missing_number([1, 2, 3, 4]) == 5


def test_missing_middle_number():
    assert program.find_missing_number([1, 2, 4, 5]) == 3


def test_two_numbers():
    assert program.find_missing_number([1]) == 2


print("All test cases passed.")