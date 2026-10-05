from importlib.machinery import SourceFileLoader

program = SourceFileLoader("even_odd", "Code/01_even_odd.py").load_module()



assert program.check_even_odd(10) == "Even"



assert program.check_even_odd(7) == "Even"



assert program.check_even_odd(0) == "Even"



assert program.check_even_odd(-8) == "Odd"



assert program.check_even_odd(-5) == "Odd"


print("All test cases passed.")