import numpy as np
from numpy.testing import assert_allclose, assert_equal


def test_equality():
    x = np.array([1, 1])
    y = np.array([2, 2])
    z = np.array([3, 3])
    assert_equal(x + y, z)


def test_equality_with_nan():
    x = np.array([1, np.nan])
    y = np.array([2, np.nan])
    z = np.array([3, np.nan])
    assert_equal(x + y, z)


def test_allclose_with_nan():
    x = np.array([1.1, np.nan])
    y = np.array([2.2, np.nan])
    z = np.array([3.3, np.nan])
    assert_allclose(x + y, z)
