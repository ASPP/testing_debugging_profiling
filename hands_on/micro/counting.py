import numpy as np


def external_match(a):
    masks = [np.array([[0, 0], [0, 1]]),
             np.array([[0, 0], [1, 0]]),
             np.array([[1, 0], [0, 0]]),
             np.array([[0, 1], [0, 0]])]
    
    for mask in masks:
        if np.all(a == mask):
            return True
    return False


def internal_match(a):
    masks = [np.array([[1, 1], [1, 0]]),
             np.array([[1, 1], [0, 1]]),
             np.array([[0, 1], [1, 1]]),
             np.array([[1, 0], [1, 1]])]
    
    for mask in masks:
        if np.all(a == mask):
            return True
    return False


def count_objects(img):
    ny, nx = img.shape

    img[[0, -1], :] = 0
    img[:, [0, -1]] = 0

    E = 0
    I = 0
    for i in range(ny-1):
        for j in range(nx-1):
            if external_match(img[i:i+2, j:j+2]):
                E += 1
            if internal_match(img[i:i+2, j:j+2]):
                I += 1
    return (E - I)/4
