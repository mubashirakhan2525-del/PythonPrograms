from importlib.machinery import SourceFileLoader

program = SourceFileLoader("word_frequency", "Code/20_word_frequency.py").load_module()


def test_word_frequency():
    assert program.word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


def test_all_unique_words():
    assert program.word_frequency("python is easy") == {
        "python": 1,
        "is": 1,
        "easy": 1
    }


def test_repeated_words():
    assert program.word_frequency("cat cat dog dog cat") == {
        "cat": 3,
        "dog": 2
    }


def test_empty_sentence():
    assert program.word_frequency("") == {}


def test_uppercase_words():
    assert program.word_frequency("Hello hello HELLO") == {
        "hello": 3
    }


print("All test cases passed.")