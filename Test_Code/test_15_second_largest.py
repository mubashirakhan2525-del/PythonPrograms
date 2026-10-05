from importlib.machinery import SourceFileLoader

program = SourceFileLoader("second_largest", "Code/15_second_largest.py").load_module()


assert program.second_largest([10, 20, 5, 8]) == 10


assert program.second_largest([4, 9, 2, 7, 5]) == 7


assert program.second_largest([10, 10, 8, 5]) == 8


assert program.second_largest([-10, -5, -8, -2]) == -5


assert program.second_largest([1, 2]) == 1


print("All test cases passed.")