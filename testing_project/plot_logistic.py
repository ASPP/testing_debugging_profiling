"""Usage:
```
plot_trajectory(100, 3.6, 0.1)
plot_bifurcation(2.5, 4.2, 0.001)
```
"""
import numpy as np
from matplotlib import pyplot as plt

from logistic import iterate_f


def plot_trajectory(n, r, x0, fname="single_trajectory.png"):
    """
    Saves a plot of a single trajectory of the logistic function

    inputs
        n: int (number of iterations)
        r: float (r value for the logistic function)
        x0: float (between 0 and 1, starting point for the iteration)
        fname: str (filename to which to save the image)

    returns
        fig, ax (matplotlib objects)
    """
    xs = iterate_f(n, x0, r)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(list(range(n)), xs)
    fig.suptitle('Logistic Function')

    fig.savefig(fname)
    return fig, ax


def plot_bifurcation(start, end, step, fname="bifurcation.png", it=100000,
                     last=300):
    """
    Saves a plot of the bifurcation diagram of the logistic function. The
    `start`, `end`, and `step` parameters define for which r values to
    calculate the logistic function. If you space them too closely, it might
    take a very long time, if you dont plot enough, your bifurcation diagram
    won't be informative. Choose wisely!

    inputs
        start, end, step:  float (which r values to calculate the logistic
                                  function for)
        fname: str (filename to which to save the image)
        it: int (how many iterations to run for each r value)
        last: int (how many of the last iterates to plot)


    returns
        fig, ax (matplotlib objects)
    """
    r_range = np.arange(start, end, step)
    x = []
    y = []

    for r in r_range:
        xs = iterate_f(it, 0.1, r)
        all_xs = xs[len(xs) - last::].copy()
        unique_xs = np.unique(all_xs)
        y.extend(unique_xs)
        x.extend(np.ones(len(unique_xs)) * r)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.scatter(x, y, s=0.1, color='k')
    ax.set_xlabel("r")
    fig.savefig(fname)
    return fig, ax
