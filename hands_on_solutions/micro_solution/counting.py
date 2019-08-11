import numpy as np
from scipy.signal import convolve2d


EXTERNAL_MASKS = [
    np.array([[0, 0], [0, 1]]),
    np.array([[0, 0], [1, 0]]),
    np.array([[1, 0], [0, 0]]),
    np.array([[0, 1], [0, 0]])
]

INTERNAL_MASKS = [
    np.array([[1, 1], [1, 0]]),
    np.array([[1, 1], [0, 1]]),
    np.array([[0, 1], [1, 1]]),
    np.array([[1, 0], [1, 1]])
]


def count_masks_match(img, masks):
    img_resc = img * 2 - 1

    masks_tot = 0
    for mask in masks:
        mask = mask * 2 - 1
        count = (convolve2d(img_resc, mask, mode='valid') == 4).sum()
        masks_tot += count
    return masks_tot


def count_objects(img):
    img[[0, -1], :] = 0
    img[:, [0, -1]] = 0

    external = count_masks_match(img, EXTERNAL_MASKS)
    internal = count_masks_match(img, INTERNAL_MASKS)

    return (external - internal) / 4
