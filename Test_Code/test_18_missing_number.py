from importlib.machinery import SourceFileLoader

program = SourceFileLoader("missing_number", "Code/18_missing_number.py").load_module()




assert program.find_missing_number([2, 3, 4, 5]) == 1


assert program.find_missing_number([1, 2, 3, 4]) == 5


assert program.find_missing_number([1, 2, 4, 5]) == 3


assert program.find_missing_number([1]) == 2


print("All test cases passed.")