from importlib.machinery import SourceFileLoader

program = SourceFileLoader("char_frequency", "Code/14_char_frequency.py").load_module()


def test_simple_string():
    assert program.character_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_repeated_character():
    assert program.character_frequency("aaa") == {
        "a": 3
    }


def test_single_character():
    assert program.character_frequency("a") == {
        "a": 1
    }


def test_empty_string():
    assert program.character_frequency("") == {}


def test_string_with_spaces():
    assert program.character_frequency("a a") == {
        "a": 2,
        " ": 1
    }


print("All test cases passed.")