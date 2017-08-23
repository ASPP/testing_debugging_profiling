import numpy as np
from numpy.testing import assert_array_equal

from noiser.utils import copy_image


def test_copy_image():
    height, width = 101, 102
    dtype = np.float32

    image = np.random.rand(height, width, 3).astype(dtype)
    copy = copy_image(image)
    assert_array_equal(copy, image)

