from importlib.machinery import SourceFileLoader

program = SourceFileLoader("common_elements", "Code/17_common_elements.py").load_module()


assert program.common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


assert program.common_elements([1, 2, 3], [4, 5, 6]) == []


assert program.common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


assert program.common_elements([1, 2, 2, 3], [2, 2, 4]) == [2]


assert program.common_elements([-1, -2, 3], [-2, 3, 5]) == [-2, 3]


print("All test cases passed.")
