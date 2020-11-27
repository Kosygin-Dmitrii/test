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


cache = {}  # Empty dictionary


def fib2(n):
    """
    fib2 with cache
    """
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


print(fib2(800))
