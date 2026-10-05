from importlib.machinery import SourceFileLoader

program = SourceFileLoader("vowels_consonants", "Code/11_vowels_consonants.py").load_module()


assert program.count_vowels_consonants("Hello") == (2, 3)


assert program.count_vowels_consonants("aeiou") == (5, 0)


assert program.count_vowels_consonants("bcdfg") == (0, 5)


assert program.count_vowels_consonants("Hello World") == (3, 7)


assert program.count_vowels_consonants("") == (0, 0)


print("All test cases passed.")