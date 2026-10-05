from importlib.machinery import SourceFileLoader

program = SourceFileLoader("primes_in_range", "Code/07_primes_in_range.py").load_module()


assert program.primes_in_range(10, 20) == [11, 13, 17, 19]


assert program.primes_in_range(1, 5) == [2, 3, 5]


assert program.primes_in_range(8, 10) == []


assert program.primes_in_range(7, 7) == [7]


assert program.primes_in_range(0, 3) == [2, 3]

print("All test cases passed.")