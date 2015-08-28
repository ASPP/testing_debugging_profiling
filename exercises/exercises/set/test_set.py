import unittest
import numpy
import set_solver


class TestSets(unittest.TestCase):

    def test_is_set(self):
        """Test set validator (Exercise 3a)."""
        cards = numpy.array([[1,1,1,2,0],
                             [0,1,2,2,2],
                             [0,1,2,2,2],
                             [0,1,2,2,2]])

        self.assertTrue(set_solver.is_set(cards, [0, 1, 2]))
        self.assertFalse(set_solver.is_set(cards, [0, 1, 3]))
        self.assertTrue(set_solver.is_set(cards, [2, 3, 4]))

    def test_find_sets(self):
        """Test solver (Exercise 3b)."""
        cards = numpy.array([[1,1,1,2,0],
                             [0,1,2,2,2],
                             [0,1,2,2,2],
                             [0,1,2,2,2]])

        set_indices = set_solver.find_sets(cards)
        self.assertEqual(len(set_indices), 2)
        self.assertTrue((0, 1, 2) in set_indices)
        self.assertTrue((2, 3, 4) in set_indices)


if __name__ == '__main__':
    unittest.main()
