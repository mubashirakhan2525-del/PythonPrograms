def sum_of_digits(number):
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    print("Sum of digits is:", sum_of_digits(number))