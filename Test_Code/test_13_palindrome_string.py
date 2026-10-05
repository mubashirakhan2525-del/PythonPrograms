from importlib.machinery import SourceFileLoader

program = SourceFileLoader("palindrome_string", "Code/13_palindrome_string.py").load_module()


assert program.is_palindrome("madam") == True


assert program.is_palindrome("hello") == False


assert program.is_palindrome("a") == True


assert program.is_palindrome("") == True


assert program.is_palindrome("noon") == True


print("All test cases passed.")