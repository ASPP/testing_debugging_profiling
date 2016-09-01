""" Tests for the factorial function. """

from factorial import factorial


def test_factorial():
    factorial_cases = [(1, 1),
                       (0, 1),
                       (5, 2*3*4*5),
                       (30, 265252859812191058636308480000000)]

    for n, fact_n in factorial_cases:
        assert factorial(n) == fact_n
