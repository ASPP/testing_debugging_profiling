import unittest
import numpy


class TestNumpyEquality(unittest.TestCase):

    def test_equality(self):
        x = numpy.array([1, 1])
        y = numpy.array([2, 2])        
        z = numpy.array([3, 3])
        self.assertEqual(x + y, z)
