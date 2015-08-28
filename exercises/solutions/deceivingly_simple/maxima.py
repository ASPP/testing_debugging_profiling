# Advanced Scientific Programming in Python
# Exercise 3


# Solution 1, only fixes the bugs without addressing the special cases
def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 1, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    If in a local maximum several elements have the same value,
    return the rightmost index.
    Example:
    >>> x = [1, 2, 2, 2, 1]
    >>> find_maxima(x)
    [3]

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %s instead' % type(x)
        raise ValueError(message)

    idx = []
    for i in range(len(x)):
        # `i` is a local maximum if the signal decreases before and after it
        # WARNING: when `i` is at the limits of the list, check it decreases
        # only in the direction where it is defined
        if ((i == 0 or x[i-1] < x[i])
            and (i+1 == len(x) or x[i+1] < x[i])):
            idx.append(i)
    return idx


# Solution 2, more complex solution that considers the special cases
# XXX I'm pretty sure there exist a more elegant and concise solution,
# to be addressed in the refatoring step once the tests pass!
def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 1, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    If in a local maximum several elements have the same value,
    return the rightmost index.
    Example:
    >>> x = [1, 2, 2, 2, 1]
    >>> find_maxima(x)
    [3]

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %s instead' % type(x)
        raise ValueError(message)

    idx = []
    up = False
    down = False
    for i in range(len(x)):
        if i == 0 or x[i-1] < x[i]:
            up = True
        elif x[i-1] > x[i]:
            up = False

        # if x[i-1] == x[i], no change

        if i+1 == len(x) or x[i+1] < x[i]:
            down = True
        elif x[i+1] > x[i]:
            down = False

        if up and down:
            idx.append(i)

    return idx
