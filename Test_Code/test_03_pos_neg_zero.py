from importlib.machinery import SourceFileLoader

program = SourceFileLoader("pos_neg_zero", "Code/03_pos_neg_zero.py").load_module()


assert program.check_number(10) == "Positive"


assert program.check_number(-5) == "Negative"


assert program.check_number(0) == "Zero"


assert program.check_number(100) == "Positive"


assert program.check_number(-100) == "Negative"


print("All test cases passed.")