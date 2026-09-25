def is_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if is_palindrome(number):
        print(number, "is a palindrome number.")
    else:
        print(number, "is not a palindrome number.")