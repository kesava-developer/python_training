from typing import List


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_palindrome(text: str) -> bool:
    """Check if the given string is a palindrome."""
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


def fibonacci_sequence(limit: int) -> List[int]:
    """Return a list of Fibonacci numbers up to the given limit."""
    if limit < 0:
        raise ValueError("limit must be non-negative")
    sequence: List[int] = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    print("factorial(5) =", factorial(5))
    print("is_palindrome('Racecar') =", is_palindrome('Racecar'))
    print("fibonacci_sequence(20) =", fibonacci_sequence(20))
