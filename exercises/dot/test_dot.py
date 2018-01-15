"""
In this exercise we want to test two testing concepts that can
be tricky:

1. testing where the numerical result is inexact, and we need
   to check that the result is approximately as expected with
   certain precision.

2. testing where we want to check that the code actually raises
   an error if the conditions are wrong. We don't want the
   tests to crash, quite the opposite: the tests must return
   success when the code reports and error, and return failure
   when the code does not report an error or reports an error
   of an unexpected type.

Finish the test functions below according to their docstrings.
"""

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
    ...

def test_size_mismatch():
    """Make sure that ValueError is raised on size mismatch

    Matrix multiplication is only possible if the horizontal dimension
    of the first matrix is equal to the vertical dimension of the other
    one.
    """
    ...
