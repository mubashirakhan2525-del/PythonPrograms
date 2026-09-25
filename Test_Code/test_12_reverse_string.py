from importlib.machinery import SourceFileLoader

program = SourceFileLoader("reverse_string", "Code/12_reverse_string.py").load_module()


def test_reverse_string():
    assert program.reverse_string("hello") == "olleh"


def test_empty_string():
    assert program.reverse_string("") == ""


def test_single_character():
    assert program.reverse_string("a") == "a"


def test_reverse_word():
    assert program.reverse_string("Python") == "nohtyP"


def test_reverse_with_spaces():
    assert program.reverse_string("hello world") == "dlrow olleh"


print("All test cases passed.")