import unittest
from maxima import find_maxima


class TestFindMaxima(unittest.TestCase):

    def test_last_element(self):
        x = [1, 2]
        idx = find_maxima(x)
        self.assertEqual(idx, [1])

    def test_first_element(self):
        x = [3, 1, 4]
        idx = find_maxima(x)
        self.assertEqual(idx, [0, 2])

    def test_equality(self):
        case_res = [([1, 2, 2, 1, 1], [2]),
                    ([1, 2, 2, 3, 1], [3]),
                    ([1, 3, 2, 2, 1], [1]),
                    ([3, 2, 2, 2, 3], [0, 4])]
        for x, desired in case_res:
            idx = find_maxima(x)
            self.assertEqual(idx, desired)

    def test_check_input(self):
        self.assertRaises(ValueError, find_maxima, 2)


if __name__ == '__main__':
    unittest.main()
