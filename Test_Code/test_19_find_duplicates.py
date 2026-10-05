from importlib.machinery import SourceFileLoader

program = SourceFileLoader("find_duplicates", "Code/19_find_duplicates.py").load_module()


assert program.find_duplicates([1, 2, 3, 2, 4, 5, 3]) == [2, 3]


assert program.find_duplicates([1, 2, 3, 4]) == []


assert program.find_duplicates([5, 5, 5, 5]) == [5]


assert program.find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]


assert program.find_duplicates([-1, -2, -1, 3, -2]) == [-1, -2]


print("All test cases passed.")