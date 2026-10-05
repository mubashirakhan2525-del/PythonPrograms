from importlib.machinery import SourceFileLoader

program = SourceFileLoader("palindrome_number", "Code/09_palindrome_number.py").load_module()


assert program.is_palindrome(121) == True


assert program.is_palindrome(123) == False


assert program.is_palindrome(7) == True


assert program.is_palindrome(11) == True


assert program.is_palindrome(100) == False


print("All test cases passed.")