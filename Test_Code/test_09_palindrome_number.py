from importlib.machinery import SourceFileLoader

program = SourceFileLoader("palindrome_number", "Code/09_palindrome_number.py").load_module()


def test_palindrome_number():
    assert program.is_palindrome(121) == True


def test_not_palindrome_number():
    assert program.is_palindrome(123) == False


def test_single_digit():
    assert program.is_palindrome(7) == True


def test_two_digit_palindrome():
    assert program.is_palindrome(11) == True


def test_number_100():
    assert program.is_palindrome(100) == False


print("All test cases passed.")