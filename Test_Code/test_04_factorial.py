from importlib.machinery import SourceFileLoader

program = SourceFileLoader("factorial", "Code/04_factorial.py").load_module()


def test_factorial_zero():
    assert program.factorial(0) == 1


def test_factorial_one():
    assert program.factorial(1) == 1


def test_factorial_five():
    assert program.factorial(5) == 120


def test_factorial_six():
    assert program.factorial(6) == 720


def test_factorial_ten():
    assert program.factorial(10) == 3628800


print("All test cases passed.")