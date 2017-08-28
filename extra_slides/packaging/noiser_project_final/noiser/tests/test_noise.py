import numpy as np
from numpy.testing import assert_allclose

from noiser.noise import white_noise


def test_white_noise():
    n_images, height, width = 201, 101, 102
    dtype = np.float32

    # Create ``n_images`` identical image.
    base_image = np.random.rand(1, height, width, 3).astype(dtype) - 0.5
    images = np.repeat(base_image, n_images, axis=0)

    std = 0.13
    noisy = white_noise(images, std=std)

    # dtype and shape are preserved.
    assert noisy.dtype == dtype
    assert noisy.shape == images.shape

    # Mean and std of noisy image match expectations.
    assert_allclose(images.mean(0), base_image[0], atol=1e-4)
    assert np.isclose((noisy - images).std(), std, atol=1e-4)
