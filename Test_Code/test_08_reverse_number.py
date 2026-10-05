from importlib.machinery import SourceFileLoader

program = SourceFileLoader("reverse_number", "Code/08_reverse_number.py").load_module()


assert program.reverse_number(12345) == 54321


assert program.reverse_number(120) == 21


assert program.reverse_number(7) == 7


assert program.reverse_number(45) == 54


assert program.reverse_number(100) == 1

print("All test cases passed.")