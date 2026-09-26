from importlib.machinery import SourceFileLoader

program = SourceFileLoader("palindrome_string", "Code/13_palindrome_string.py").load_module()


def test_palindrome_word():
    assert program.is_palindrome("madam") == True


def test_non_palindrome_word():
    assert program.is_palindrome("hello") == False


def test_single_character():
    assert program.is_palindrome("a") == True


def test_empty_string():
    assert program.is_palindrome("") == True


def test_palindrome_with_even_characters():
    assert program.is_palindrome("noon") == True


print("All test cases passed.")