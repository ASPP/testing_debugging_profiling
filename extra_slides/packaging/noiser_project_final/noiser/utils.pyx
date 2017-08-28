import numpy as np
cimport numpy as np


def copy_image(np.ndarray img):
    cdef int h = img.shape[0]
    cdef int w = img.shape[1]
    cdef int c = img.shape[2]
    cdef np.ndarray copy = np.empty([h, w, c], dtype=img.dtype)

    for i in range(h):
        for j in range(w):
            for k in range(c):
                copy[i, j, k] = img[i, j, k]
    return copy
