from numbers import Integral  
# integral is adjective form of integer, not a calculus integral


def fib(n):
    """Return the n-th Fibonacci number."""
    if not isinstance(n, Integral):
        raise TypeError(
            f"fib expects an integer, not a {type(n).__name__}"
        )
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# useful to have a blank line after the function
