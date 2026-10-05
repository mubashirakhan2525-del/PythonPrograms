from importlib.machinery import SourceFileLoader

program = SourceFileLoader("remove_duplicates", "Code/16_remove_duplicates.py").load_module()


assert program.remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]


assert program.remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]


assert program.remove_duplicates([5, 5, 5, 5]) == [5]


assert program.remove_duplicates([]) == []


assert program.remove_duplicates([-1, -1, 2, 2, 3]) == [-1, 2, 3]


print("All test cases passed.")
