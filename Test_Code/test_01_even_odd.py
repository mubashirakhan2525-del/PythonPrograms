import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("even_odd", "Code/01_even_odd.py").load_module()

assert program.check_even_odd(2) == "Even"
assert program.check_even_odd(5) == "Odd"
assert program.check_even_odd(0) == "Even"
assert program.check_even_odd(-4) == "Even"
assert program.check_even_odd(-7) == "Odd"

print("All test cases passed.")