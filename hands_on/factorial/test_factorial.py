""" Tests for the factorial function. """

import unittest
from factorial import factorial


class FactorialTestCase(unittest.TestCase):
    
    def test_factorial(self):
        factorial_cases = [(1, 1),
                           (0, 1),
                           (5, 2*3*4*5),
                           (30, 265252859812191058636308480000000)]
        for n, fact_n in factorial_cases:
            self.assertEqual(factorial(n), fact_n)


if __name__ == '__main__':
    unittest.main()
