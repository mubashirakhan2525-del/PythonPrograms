from importlib.machinery import SourceFileLoader

program = SourceFileLoader("char_frequency", "Code/14_char_frequency.py").load_module()


assert program.character_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


assert program.character_frequency("aaa") == {
        "a": 3
    }


assert program.character_frequency("a") == {
        "a": 1
    }


assert program.character_frequency("") == {}


assert program.character_frequency("a a") == {
        "a": 2,
        " ": 1
    }


print("All test cases passed.")