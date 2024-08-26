import numpy as np
from numpy.testing import assert_allclose

from logistic import iterate_f
from logistic_fit import fit_r


SEED = 42


def test_logistic_fit():
    r = 3.123
    x0 = 0.322
    xs = iterate_f(it=27, x0=x0, r=r)

    assert_allclose(r, fit_r(xs), atol=1e-3)


def test_logistic_fit_randomized():
    random_state = np.random.RandomState(SEED)
    # We test for 100 random values of x0 and r, to make sure that the function works in general.
    for _ in range(100):
        x0 = random_state.uniform(0.0001, 0.9999)
        # Round `r` to 1/1000 to make sure that it matches the precision of the fit_r function,
        # so that r can be exactly recovered.
        r = round(random_state.uniform(0.001, 3.999), 3)
        xs = iterate_f(it=17, x0=x0, r=r)

        assert_allclose(r, fit_r(xs), atol=1e-3)
