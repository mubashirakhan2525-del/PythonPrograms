from importlib.machinery import SourceFileLoader

program = SourceFileLoader("largest_of_three", "Code/02_largest_of_three.py").load_module()

assert program.largest_of_three(10, 20, 15) == 20
assert program.largest_of_three(5, 3, 2) == 5
assert program.largest_of_three(1, 7, 9) == 9
assert program.largest_of_three(-2, -5, -1) == -1
assert program.largest_of_three(10, 10, 5) == 10

print("All test cases passed.")