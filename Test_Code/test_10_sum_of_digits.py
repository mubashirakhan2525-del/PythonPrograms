from importlib.machinery import SourceFileLoader

program = SourceFileLoader("sum_of_digits", "Code/10_sum_of_digits.py").load_module()


assert program.sum_of_digits(12345) == 15


assert program.sum_of_digits(7) == 7


assert program.sum_of_digits(0) == 0


assert program.sum_of_digits(45) == 9


assert program.sum_of_digits(100) == 1


print("All test cases passed.")
