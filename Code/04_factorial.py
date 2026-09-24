def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial is:", factorial(number))