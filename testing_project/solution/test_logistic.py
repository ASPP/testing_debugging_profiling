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

@pytest.mark.parametrize("x, r, expected", [
    (0.1, 2.2, 0.198),
    (0.2, 3.4, 0.544),
    (0.5, 2, 0.5),
])
def test_f_parametrized(x, r, expected):
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


def test_iterate_f():
    # Test cases are (x, r, it, expected)
    cases = [
        (0.1, 2.2, 1, [0.1, 0.198]),
        (0.2, 3.4, 4, [0.2, 0.544, 0.843418, 0.449019, 0.841163]),
        (0.5, 2, 3, [0.5, 0.5, 0.5, 0.5]),
    ]
    for x, r, it, expected in cases:
        result = iterate_f(it=it, x0=x, r=r)
        assert_allclose(result, expected, rtol=1e-5)


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


def test_chaotic_behavior():
    # 2) Orbits must be bounded: check that all values are between 0 and 1
    # 3) Orbits must be aperiodic: check that the last 1000 values are all different
    r = 3.9
    x0 = 0.5
    xs = iterate_f(it=2000, x0=x0, r=r)
    assert np.all((xs >= 0) & (xs <= 1))
    assert len(np.unique(xs[-1000:])) == 1000
    # quite unlikely but might need to loosen this constraint, as 2 could be
    # the same by accident. 
    assert len(np.unique(xs[-1000:])) > 500


# BONUS exercise: test for sensitive dependence on initial conditions (SDIC)
def test_butterfly_effect():
    # f is a function and x0 and y0 are two possible seeds. If f has SDIC then:
    # there is a number delta such that for any x0 there is a y0 that is not
    # more than init_error away from x0, where the initial condition y0 has the
    # property that there is some integer n such that after n iterations, the
    # orbit is more than delta away from the orbit of x0. That is |xn-yn| > delta
    r = 3.9
    x0 = 0.5
    init_error = 1e-5
    delta = 0.1
    xs = iterate_f(it=100, x0=x0, r=r)
    y0 = x0 + init_error
    ys = iterate_f(it=100, x0=y0, r=r)
    assert np.any(np.abs(xs - ys) > delta)

# Bonus Exercise 4 -- The Butterfly Effect

# For the same value of r, test the sensitive dependence on initial conditions, a.k.a. the butterfly effect. Use the following definition of SDIC.

#     f is a function and x0 and y0 are two possible seeds. If f has SDIC then: there is a number delta such that for any x0 there is a y0 that is not more than init_error away from x0, where the initial condition y0 has the property that there is some integer n such that after n iterations, the orbit is more than delta away from the orbit of x0. That is |xn-yn| > delta
