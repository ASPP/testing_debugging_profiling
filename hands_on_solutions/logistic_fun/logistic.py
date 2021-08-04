import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
    """
    write a funtion that takes r and x as input and returns r*x*(1-x)
    """
    return r*x*(1-x)

def iterate_f(it, xi, r):
    """
    write a function that takes a number of iterations "it", a starting value,
    and a parameter value for r. It should execute f repeatedly (it times), each
    time using the last result of f as the new input to f. Append each iteration's
    result to a list. Finally, convert the list into a numpy array and return it.
    """
    l = []
    x = xi
    for i in range(it):
        l.append(x)
        x = f(x, r)
    return np.array(l)