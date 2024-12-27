def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    try:
        # Kullanıcıdan bir sayı al
        number = int(input("Please enter a positive integer to calculate its factorial: "))

        if number < 0:
            print("Please enter a positive integer.")
        else:
            fact = factorial(number)
            print(f"The factorial of {number} is {fact}.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
