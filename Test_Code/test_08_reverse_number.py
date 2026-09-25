from importlib.machinery import SourceFileLoader

program = SourceFileLoader("reverse_number", "Code/08_reverse_number.py").load_module()


def test_reverse_number():
    assert program.reverse_number(12345) == 54321


def test_reverse_number_with_zero():
    assert program.reverse_number(120) == 21


def test_single_digit():
    assert program.reverse_number(7) == 7


def test_reverse_two_digit_number():
    assert program.reverse_number(45) == 54


def test_number_100():
    assert program.reverse_number(100) == 1

print("All test cases passed.")