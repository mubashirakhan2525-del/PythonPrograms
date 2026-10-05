from importlib.machinery import SourceFileLoader

program = SourceFileLoader("word_frequency", "Code/20_word_frequency.py").load_module()


assert program.word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


assert program.word_frequency("python is easy") == {
        "python": 1,
        "is": 1,
        "easy": 1
    }


assert program.word_frequency("cat cat dog dog cat") == {
        "cat": 3,
        "dog": 2
    }


assert program.word_frequency("") == {}


assert program.word_frequency("Hello hello HELLO") == {
        "hello": 3
    }


print("All test cases passed.")