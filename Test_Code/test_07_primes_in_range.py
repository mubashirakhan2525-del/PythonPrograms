from importlib.machinery import SourceFileLoader

program = SourceFileLoader("primes_in_range", "Code/07_primes_in_range.py").load_module()


def test_primes_in_range():
    assert program.primes_in_range(10, 20) == [11, 13, 17, 19]


def test_small_range():
    assert program.primes_in_range(1, 5) == [2, 3, 5]


def test_range_with_no_primes():
    assert program.primes_in_range(8, 10) == []


def test_single_prime():
    assert program.primes_in_range(7, 7) == [7]


def test_range_starting_from_zero():
    assert program.primes_in_range(0, 3) == [2, 3]