import cmath


def fibonacci(n):
    """
    Recursive function to compute the nth value of the fibonacci sequence,
    where each number equals the sum of the two numbers before it.
    The sequence of numbers: 0,1,1,2,3,5,8,13,21,...

    :param n: Index of the fibonacci sequence to compute.
    :return: Value of fibonacci sequence at nth index.
    """
    if n < 0:
        raise ValueError("Index must be a positive integer")

    # First Fibonacci number is 0
    elif n == 0:
        return 0

    # Second Fibonacci number is 1
    elif n == 1:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# def fibonacci(n):
#     """
#     Function to compute the nth value of the fibonacci sequence,
#     where each number equals the sum of the two numbers before it.
#     The sequence of numbers: 0,1,1,2,3,5,8,13,21,...
#
#     Optimized for memory usage.
#
#     :param n: Index of the fibonacci sequence to compute.
#     :return: Value of fibonacci sequence at nth index.
#     """
#     a = 0
#     b = 1
#
#     if n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b


def quadratic(a, b, c):
    """
    Function that gives the solutions of the general quadratic equation ax2 + bx + c = 0
    and that is usually written in the form x = (-b ± √(b2 − 4ac))/(2a). Implemented
    using cmath to support complex numbers.

    :param a: Coefficient of the quadratic term.
    :param b: Coefficient of the x term.
    :param c: Constant
    :return: x-intercepts of the equation, i.e. where the curve crosses the x-axis
    """

    # The Discriminant
    d = (b ** 2) - (4 * a * c)

    # The Solutions
    solution1 = (-b - cmath.sqrt(d)) / (2 * a)
    solution2 = (-b + cmath.sqrt(d)) / (2 * a)
    return solution1, solution2
