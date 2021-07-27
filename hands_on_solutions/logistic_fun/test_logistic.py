import numpy as np
from logistic import iterate_f
import pytest

@pytest.mark.parametrize("x0", [0.1, 0.5,0.9])
def test_convergence(x0):
    expected_value = 1/3
    l = iterate_f(1000, x0, 1.5)
    conv_value = np.mean(l[-10:-1])

    assert np.isclose(expected_value, conv_value)


def test_stability():
    x0 = 1/3
    expected_value = 1/3
    l = iterate_f(1000, x0, 1.5)
    conv_value = np.mean(l[-10:-1])
    assert np.isclose(expected_value, conv_value)

def test_divergence():
    rand_state = np.random.RandomState(8393)
    r = rand_state.uniform(4,6)
    x0 = rand_state.rand()
    n = 10
    l_x = iterate_f(n, x0, r)
    l_x_diff = np.diff(l_x)
    err = 0.000001
    assert not all(l_x_diff[-10:-1]>err)

@pytest.mark.parametrize("i", range(10))
def test_fuzzy_sdic(i):
    """
    there is a number delta such that for any x0 there is a y0 that is not more 
    than init_error away from x0, when the initial condition y0 has the property
    that there is an int n wuch that after n iterations the orbit is more than 
    delta away from the orbit of x0. That is 
    |xn-yn| > delta
    """
    rand_state = np.random.RandomState(8393)
    delta = rand_state.rand()
    x0 = rand_state.rand()
    init_error = rand_state.rand()
    y0max = x0 + init_error
    n = 10000
    l_x = iterate_f(n, x0, 4)
    l_y = iterate_f(n, y0max, 4)
    assert any(abs(l_x - l_y)>delta)


