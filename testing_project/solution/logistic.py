import numpy as np


def f(x, r):
    """ Compute the logistic map for a given value of x and r. """
    return r * x * (1 - x)


def iterate_f(it, x0, r):
    """ Generate a population trajectory.

    Takes a number of iterations `it`, a starting value, x0,
    and a parameter value for r. It executes f repeatedly (it times),
    each time using the last result of f as the new input to f. Append each
    iteration's result to a list l. Finally, convert the list into a numpy
    array and return it.
    """
    x = x0
    xs = [x0]
    for _ in range(it):
        x = f(x, r)
        xs.append(x)

    return np.array(xs)
