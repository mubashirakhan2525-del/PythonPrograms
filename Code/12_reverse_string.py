def reverse_string(text):
    reverse = ""

    for character in text:
        reverse = character + reverse

    return reverse


if __name__ == "__main__":
    text = input("Enter a string: ")

    print("Reversed string is:", reverse_string(text))