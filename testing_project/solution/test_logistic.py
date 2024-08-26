import numpy as np
from numpy.testing import assert_allclose
import pytest

from logistic import f, iterate_f


def test_f():
    # Test cases are (x, r, expected)
    cases = [
        (0.1, 2.2, 0.198),
        (0.2, 3.4, 0.544),
        (0.5, 2, 0.5),
    ]
    for x, r, expected in cases:
        result = f(x, r)
        assert_allclose(result, expected)


def test_f_corner_cases():
    # Test cases are (x, r, expected)
    cases = [
        (0, 1.1, 0),
        (1, 3.7, 0),
    ]
    for x, r, expected in cases:
        result = f(x, r)
        assert_allclose(result, expected)


def test_random_convergence():
    SEED = 42
    random_state = np.random.RandomState(SEED)
    r = 1.5
    for _ in range(100):
        x0 = random_state.uniform(0.0000001, 0.9999999)
        xs = iterate_f(it=100, x0=x0, r=r)
        assert np.isclose(xs[-1], 1 / 3)

# SEED = 42
# @pytest.fixture
# def random_state():
#     print(f"Using seed {SEED}")
#     random_state = np.random.RandomState(SEED)
#     return random_state


#@pytest.mark.xfail
def test_random_convergence_decorator(random_state):
    r = 1.5
    for _ in range(100):
        x0 = random_state.uniform(0.0000001, 0.9999999)
        xs = iterate_f(it=100, x0=x0, r=r)
        assert np.isclose(xs[-1], 1 / 3)