def distinct(number):
    """Checks if the digits of a natural number are distinct"""
    seen = []

    while number:
        digit = number % 10
        if digit in seen:
            return False

        seen.append(digit)

        # Remove the last digit from the number
        number //= 10

    return True


def solve(left, right):
    """Searches for the first number with distinct digits
    in the interval [left, right]."""
    for number in range(left, right + 1):
        if distinct(number):
            print(number)
            return

    print(-1)


a, b = input().split()
a, b = int(a), int(b)
solve(a, b)
