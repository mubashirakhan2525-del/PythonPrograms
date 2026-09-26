from importlib.machinery import SourceFileLoader

program = SourceFileLoader("even_odd", "Code/01_even_odd.py").load_module()


def test_even_number():
    assert program.check_even_odd(10) == "Even"


def test_odd_number():
    assert program.check_even_odd(7) == "Odd"


def test_zero():
    assert program.check_even_odd(0) == "Even"


def test_negative_even_number():
    assert program.check_even_odd(-8) == "Even"


def test_negative_odd_number():
    assert program.check_even_odd(-5) == "Odd"


print("All test cases passed.")