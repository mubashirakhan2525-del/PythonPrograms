from importlib.machinery import SourceFileLoader

program = SourceFileLoader("prime_number", "Code/06_prime_number.py").load_module()


def test_prime_number():
    assert program.is_prime(7) == True


def test_not_prime_number():
    assert program.is_prime(8) == False


def test_two_is_prime():
    assert program.is_prime(2) == True


def test_one_is_not_prime():
    assert program.is_prime(1) == False


def test_zero_is_not_prime():
    assert program.is_prime(0) == False