def reverse_number(number):
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    print("Reversed number is:", reverse_number(number))