import numpy as np

from pyanno import voting
from pyanno.voting import MISSING_VALUE as MV


def test_labels_count():
    annotations = [
        [1,  2, MV, MV],
        [MV, MV,  3,  3],
        [MV,  1,  3,  1],
        [MV, MV, MV, MV],
    ]
    nclasses = 5
    expected = [0, 3, 1, 3, 0]
    result = voting.labels_count(annotations, nclasses)
    assert result == expected


def test_majority_vote():
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
    assert result == expected


def test_majority_vote_empty_item():
    # Test for former bug: majority vote with row of invalid annotations fails
    annotations = np.array(
        [[1, 2, 3],
         [MV, MV, MV],
         [1, 2, 2]]
    )
    expected = [1, MV, 2]
    result = voting.majority_vote(annotations)
    assert result == expected
