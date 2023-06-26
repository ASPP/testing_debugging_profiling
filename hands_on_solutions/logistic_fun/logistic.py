import numpy as np


def f(x, r):
    """
    takes r and x as input and returns r*x*(1-x)
    """
    return r * x * (1 - x)


def iterate_f(it, xi, r):
    """
    takes a number of iterations `it`, a starting value,
    and a parameter value for r. It should execute f repeatedly (it times),
    each time using the last result of f as the new input to f. Append each
    iteration's result to a list l. Finally, convert the list into a numpy
    array and return it.
    """
    x = xi
    xs = []
    for _ in range(it):
        x = f(x, r)
        xs.append(x)

    return np.array(xs)
