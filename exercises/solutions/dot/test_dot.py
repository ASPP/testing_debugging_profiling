import numpy as np

import dot

import pytest

def test_transposed():
    """Make sure that multiplication of transposed matrices

    x × y = (y.T × x.T).T

    (where .T means that the matrix is transposed, i.e. flipped
    around the diagonal.)

    Create two sample matrices using numpy.random.random, and
    verify that the transposed result of multiplication of the
    tranposed matrices gives the same result as the original
    multiplication.
    """
    
    x = np.array([[1, 4, 3],
                  [2, -1, 12]])
    y = np.array([[32, 12, 8],
                  [0, 5, 8],
                  [-3, -2, 4]])

    z1 = dot.dot(x, y)
    z2 = dot.dot(y.T, x.T).T

    assert np.allclose(z1, z2)

def test_size_mismatch():
    """Make sure that ValueError is raised on size mismatch

    Matrix multiplication is only possible if the horizontal dimension
    of the first matrix is equal to the vertical dimension of the other
    one.
    """
    with pytest.raises(ValueError):
        dot.dot(np.zeros((3,2)), np.zeros((3,2)))
