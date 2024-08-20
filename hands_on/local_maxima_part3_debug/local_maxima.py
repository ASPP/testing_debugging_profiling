def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    maxima = []

    len_x = len(x)
    if len_x == 0:
        return maxima

    maxima = check_first_element(x, maxima)
    maxima = check_last_element(x, maxima)

    # Check numbers in between
    i = 1
    while i < len_x - 1:
        if x[i] > x[i - 1]:
            # We have found a potential maximum or start of a plateau
            plateau_start = i
            while i < len_x - 1 and x[i] == x[i + 1]:
                i += 1
            plateau_end = i
            if x[plateau_end] > x[plateau_end + 1]:
                maxima.append(plateau_start)
        i += 1
    return maxima


def check_first_element(x, maxima):
    if x[0] > x[1]:
        maxima.append(0)
    return maxima


def check_last_element(x, maxima):
    if x[-1] > x[-2]:
        maxima.append(len(x) - 1)
    return maxima


if __name__ == "__main__":
    result = find_maxima([1, 2, 2, 1])
    print(result)
