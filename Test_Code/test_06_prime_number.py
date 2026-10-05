from importlib.machinery import SourceFileLoader

program = SourceFileLoader("prime_number", "Code/06_prime_number.py").load_module()


assert program.is_prime(7) == True


assert program.is_prime(8) == False


assert program.is_prime(2) == True


assert program.is_prime(1) == False


assert program.is_prime(0) == False

print("All test cases passed.")