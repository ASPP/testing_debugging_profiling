import unittest
import numpy


class TestVar(unittest.TestCase):

    def test_var_deterministic(self):
        x = numpy.array([-2.0, 2.0])
        expected = 4.0
        self.assertAlmostEqual(numpy.var(x), expected)

    def test_var_fuzzing(self):
        rand_state = numpy.random.RandomState(8393)

        N, D = 100000, 5
        # Goal variances: [0.1 ,  0.45,  0.8 ,  1.15,  1.5]
        expected = numpy.linspace(0.1, 1.5, D)

        # Test multiple times with random data
        for _ in range(20):
            # Generate random, D-dimensional data
            x = rand_state.randn(N, D) * numpy.sqrt(expected)
            variance = numpy.var(x, axis=0)
            numpy.testing.assert_array_almost_equal(variance, expected, 1)
