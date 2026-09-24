def fibonacci_series(number):
    series = []

    a = 0
    b = 1

    for i in range(number):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    number = int(input("Enter the number of terms: "))

    if number < 0:
        print("Please enter a non-negative number.")
    else:
        print("Fibonacci series:", fibonacci_series(number))