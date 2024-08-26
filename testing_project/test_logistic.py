from numpy.testing import assert_allclose

from logistic import f

# Add here your test for the logistic map


def test_f_corner_cases():
    # Test cases are (x, r, expected)
    cases = [
        (0, 1.1, 0),
        (1, 3.7, 0),
    ]
    for x, r, expected in cases:
        result = f(x, r)
        assert_allclose(result, expected)
