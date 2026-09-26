def is_palindrome(text):
    reverse = ""

    for character in text:
        reverse = character + reverse

    if text == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    text = input("Enter a string: ")

    if is_palindrome(text):
        print(text, "is a palindrome string.")
    else:
        print(text, "is not a palindrome string.")