def find_missing_number(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2

    actual_total = 0

    for number in numbers:
        actual_total = actual_total + number

    return total - actual_total


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Missing number is:", find_missing_number(numbers))