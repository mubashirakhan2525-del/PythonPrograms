from importlib.machinery import SourceFileLoader

program = SourceFileLoader("vowels_consonants", "Code/11_vowels_consonants.py").load_module()


def test_vowels_and_consonants():
    assert program.count_vowels_consonants("Hello") == (2, 3)


def test_all_vowels():
    assert program.count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert program.count_vowels_consonants("bcdfg") == (0, 5)


def test_with_spaces():
    assert program.count_vowels_consonants("Hello World") == (3, 7)


def test_empty_string():
    assert program.count_vowels_consonants("") == (0, 0)


print("All test cases passed.")