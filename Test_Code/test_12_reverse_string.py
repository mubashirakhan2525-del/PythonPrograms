from importlib.machinery import SourceFileLoader

program = SourceFileLoader("reverse_string", "Code/12_reverse_string.py").load_module()


assert program.reverse_string("hello") == "olleh"


assert program.reverse_string("") == ""


assert program.reverse_string("a") == "a"


assert program.reverse_string("Python") == "nohtyP"


assert program.reverse_string("hello world") == "dlrow olleh"


print("All test cases passed.")