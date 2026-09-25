from importlib.machinery import SourceFileLoader

program = SourceFileLoader("sum_of_digits", "Code/10_sum_of_digits.py").load_module()


def test_sum_of_digits():
    assert program.sum_of_digits(12345) == 15


def test_single_digit():
    assert program.sum_of_digits(7) == 7


def test_zero():
    assert program.sum_of_digits(0) == 0


def test_two_digit_number():
    assert program.sum_of_digits(45) == 9


def test_number_100():
    assert program.sum_of_digits(100) == 1


print("All test cases passed.")
