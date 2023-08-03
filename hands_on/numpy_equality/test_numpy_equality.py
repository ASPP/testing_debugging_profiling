import numpy as np


def test_equality():
    x = np.array([1, 1])
    y = np.array([2, 2])
    z = np.array([3, 3])
    assert x + y == z


def test_equality_with_nan():
    x = np.array([1, np.nan])
    y = np.array([2, np.nan])
    z = np.array([3, np.nan])
    assert x + y == z


def test_allclose_with_nan():
    x = np.array([1.1, np.nan])
    y = np.array([2.2, np.nan])
    z = np.array([3.3, np.nan])
    assert x + y == z
