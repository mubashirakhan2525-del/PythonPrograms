from importlib.machinery import SourceFileLoader

program = SourceFileLoader("fibonacci_series", "Code/05_fibonacci_series.py").load_module()


def test_zero_terms():
    assert program.fibonacci_series(0) == []


def test_one_term():
    assert program.fibonacci_series(1) == [0]


def test_two_terms():
    assert program.fibonacci_series(2) == [0, 1]


def test_five_terms():
    assert program.fibonacci_series(5) == [0, 1, 1, 2, 3]


def test_seven_terms():
    assert program.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]


print("All test cases passed.")
