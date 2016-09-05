import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal


def test_deterministic():
    nsamples = 1000

    samples = np.random.multinomial(nsamples, [0.0, 1.0, 0.0])
    assert_array_equal(samples, np.array([0, nsamples, 0], dtype='i'))

    samples = np.random.multinomial(nsamples, [1.0, 0.0, 1.0])
    samples[1] == 0


def test_fuzzing():
    nsamples = 100000
    p = [0.1, 0.3, 0.2, 0.4]

    samples = np.random.multinomial(nsamples, p)
    freq = samples / float(nsamples)

    assert_array_almost_equal(p, freq, 2)
