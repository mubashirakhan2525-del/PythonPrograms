from importlib.machinery import SourceFileLoader

program = SourceFileLoader("largest_of_three", "Code/02_largest_of_three.py").load_module()


assert program.largest_of_three(10, 5, 3) == 10


assert program.largest_of_three(4, 12, 7) == 12



assert program.largest_of_three(2, 6, 15) == 15


assert program.largest_of_three(5, 5, 3) == 5


assert program.largest_of_three(-10, -3, -7) == -3


print("All test cases passed.")