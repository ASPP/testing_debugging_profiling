import unittest
import numpy as np

from pyanno import voting
from pyanno.voting import MISSING_VALUE as MV


class TestVoting(unittest.TestCase):

    def test_labels_count(self):
        annotations = [
            [ 1,  2, MV, MV],
            [MV, MV,  3,  3],
            [MV,  1,  3,  1],
            [MV, MV, MV, MV],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses)
        self.assertEqual(result, expected)

    def test_majority_vote(self):
        annotations = [
            [1, 2, 2, MV],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [MV, 2, 3, 1],
            [MV, MV, MV, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_majority_vote_empty_item(self):
        # Bug: majority vote with row of invalid annotations fails
        annotations = np.array(
            [[1, 2, 3],
             [MV, MV, MV],
             [1, 2, 2]]
        )
        expected = [1, MV, 2]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_labels_count_no_valid_observations(self):
        annotations = [
            [MV, MV],
            [MV, MV],
        ]
        with self.assertRaises(voting.PyannoValueError):
             voting.labels_count([], 3)
        with self.assertRaises(voting.PyannoValueError):
             voting.labels_count(annotations, 3)

    def test_labels_count_non_default_missing_values(self):
        mv = -999
        annotations = [
            [ 1,  2, mv, mv],
            [mv, mv,  3,  3],
            [mv,  1,  3,  1],
            [mv, mv, mv, mv],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses, missing_value=mv)
        self.assertEqual(result, expected)

    def test_majority_vote_non_deafult_missing_value(self):
        mv = -999
        annotations = [
            [1, 2, 2, mv],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [mv, 2, 3, 1],
            [mv, mv, mv, 3],
            [mv, mv, mv, mv],
        ]
        expected = [2, 2, 1, 3, 1, 3, mv]
        result = voting.majority_vote(annotations, missing_value=mv)
        self.assertEqual(expected, result)

    def test_labels_frequency(self):
        annotations = [
            [ 1,  2, MV, MV],
            [MV, MV,  3,  3],
            [MV,  1,  3,  1],
            [MV, MV, MV, MV]
        ]

        nclasses = 5
        expected = np.array([0., 3., 1., 3., 0.]) / 7.
        result = voting.labels_frequency(annotations, nclasses)
        np.testing.assert_almost_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
