import numpy as np

def dot(x, y):
    if x.shape[1] != y.shape[0]:
        raise ValueError

    out = np.zeros((x.shape[0], y.shape[1]))

    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            for k in range(x.shape[1]):
                out[i, j] += x[i, k] * y[k, j]

    return out
