import numpy as np
from logistic import f, iterate_f
import pytest

# Exercise 1: write a basic test, that checks that once a point is on the attractor
# it doesnt move off it! For an r = 1.5 the attracting fixed point is at 1/3!
def test_stability():
    """
    Checks that if we iterate on an attractor, the output is the same as the
    input
    """
    x0 = 1/3
    expected_value = 1/3
    r = 1.5
    result = f(x0, r)
    assert np.isclose(expected_value, result)

# Exercise 2: Now write a test for checking that with different starting values
# the trajectories all converge on the same attractor. Use the same r value as
# above but use parametrize to try a few different starting values.
@pytest.mark.parametrize("x0", [0.1, 0.5,0.9])
def test_convergence(x0):
    """
    Checks that for a specific r < 3, given different initial values x0, all
    converge to the same attractor after 1000 iterations.
    """
    expected_value = 1/3
    r = 1.5
    l = iterate_f(1000, x0, 1.5)
    conv_value = np.mean(l[-10:-1])
    assert np.isclose(expected_value, conv_value)

# Exercise 3: trajectories using r values above 4 diverge to negative infinity.
# pick an r value above 5 and check that a few iterations later the outcome is
# -inf for different starting values.
# Exercise 3.2: expand your test to use numerical fuzzing to pick an arbitrary
# value of r > 4.
#@pytest.mark.parametrize("n", range(10))
@pytest.mark.parametrize("x0", [0.1, 0.5,0.8])
def test_divergence(x0):
    """
    Checks that for values of r > 4, given different initial values x0, all
    diverge to infinity after 1000 iterations.
    """
    r = np.random.uniform(low=4, high=15)
    print(r)
    expected_value = -np.inf
    #r = 5
    l = iterate_f(1000, x0, r)
    assert np.isclose(expected_value, l[-1])

# Exercise 4: r values or 3 < r > 4 have some interesting properties. A chaotic
# trajectory doesn't diverge but also doesn't converge. Write a test that checks
# that after a lot (e.g. 100000) of iterations the last 100 are all different.
# use r=3.8.
# Exercise 4.2: parametrize your test with some other r values: like 3.001,
# and 3.453. Your test should fail. Why? Use the plotting function
# `plot_trajectory` to find out what is going on.

@pytest.mark.xfail
@pytest.mark.parametrize("r", [3.8, 3.001, 3.453])
def test_aperiodic(r):
    """
    Checks that for a specific 3 < r > 4 trajectories become chaotic
    """
    #r = 3.8
    l = iterate_f(100000, 0.01, r)
    last = l[-101:-1]
    assert len(np.unique(last))==100

# Then mark your test as expected to fail.

# Exercise 5: To test chaotic behavior we will need to be a bit more advanced.
# Let's test that what we're seeing is actually chaos:
# - orbits mus be bounded, i.e. not diverge: you can use your divergence code for this
# - orbits must be aperiodic, i.e. only values of r that pass the test_aperiodic function can qualify
# - sensitive dependence on initial conditions
# - it has to be deterministic
# Lets write tests for the last two!
# Exercise 5.1: Look at the bifurcation plot and single trajectory plot
# and pick an r value that you think will likely yield chaos. Then write a test
# to verify that the trajectory is deterministic.

def test_determinism():
    x0 = 1/3
    r = 3.8
    result1 = f(x0, r)
    result2 = f(x0, r)
    assert np.allclose(result1, result2)

# Exercise 5.2: for the same r value, test the sensitive dependence on initial
# conditions, or the butterfly effect. Use the following definition of SDIC.

def test_fuzzy_sdic():
    """
    `f` is a function and `x0` and `y0` are two possible seeds.
    If `f` has SDIC then:
    there is a number `delta` such that for any `x0` there is a `y0` that is not
    more than `init_error` away from `x0`, where the initial condition `y0` has
    the property that there is some integer n such that after n iterations, the
    orbit is more than `delta` away from the orbit of `x0`. That is
    |xn-yn| > delta
    """
    deltas = np.random.rand(100)
    result_list = []
    for delta in deltas:
        x0 = np.random.rand()
        init_error = np.random.rand()
        y0max = x0 + init_error
        n = 10000
        l_x = iterate_f(n, x0, 3.8)
        l_y = iterate_f(n, y0max, 3.8)
        result_list.append(any(abs(l_x - l_y)>delta))
    assert any(result_list)