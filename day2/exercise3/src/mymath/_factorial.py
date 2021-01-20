"""A simple factorial implementation"""


def factorial(n: int) -> int:
    """Computes the factorial of the given number.

    Parameters
    ----------
    n : int
        Value to compute the factorial of.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
