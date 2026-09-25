def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for character in text.lower():
        if character.isalpha():
            if character in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1

    return vowels, consonants


if __name__ == "__main__":
    text = input("Enter a string: ")

    vowels, consonants = count_vowels_consonants(text)

    print("Vowels:", vowels)
    print("Consonants:", consonants)