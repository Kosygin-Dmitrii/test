"""
fibonacci numbers
"""


def fib1(n):
    """
    fib1 recursion
    """
    assert n >= 0   # Checking for positivity
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


print(fib1(8))


