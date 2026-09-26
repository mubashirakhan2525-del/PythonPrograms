def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Second largest number is:", second_largest(numbers))