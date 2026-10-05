from importlib.machinery import SourceFileLoader

program = SourceFileLoader("factorial", "Code/04_factorial.py").load_module()


assert program.factorial(0) == 1


assert program.factorial(1) == 1


assert program.factorial(5) == 120


assert program.factorial(6) == 720


assert program.factorial(10) == 3628800


print("All test cases passed.")