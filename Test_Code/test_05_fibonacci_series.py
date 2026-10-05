from importlib.machinery import SourceFileLoader

program = SourceFileLoader("fibonacci_series", "Code/05_fibonacci_series.py").load_module()


assert program.fibonacci_series(0) == []


assert program.fibonacci_series(1) == [0]


assert program.fibonacci_series(2) == [0, 1]


assert program.fibonacci_series(5) == [0, 1, 1, 2, 3]


assert program.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]


print("All test cases passed.")
