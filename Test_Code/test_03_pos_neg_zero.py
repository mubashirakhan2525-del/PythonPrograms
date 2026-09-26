from importlib.machinery import SourceFileLoader

program = SourceFileLoader("pos_neg_zero", "Code/03_pos_neg_zero.py").load_module()


def test_positive_number():
    assert program.check_number(10) == "Positive"


def test_negative_number():
    assert program.check_number(-5) == "Negative"


def test_zero():
    assert program.check_number(0) == "Zero"


def test_large_positive_number():
    assert program.check_number(100) == "Positive"


def test_large_negative_number():
    assert program.check_number(-100) == "Negative"


print("All test cases passed.")