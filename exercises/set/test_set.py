import numpy
import set_solver


def test_is_set():
    """Test set validator (Exercise 3a)."""
    cards = numpy.array([[1,1,1,2,0],
                         [0,1,2,2,2],
                         [0,1,2,2,2],
                         [0,1,2,2,2]])

    assert set_solver.is_set(cards, [0, 1, 2])
    assert not set_solver.is_set(cards, [0, 1, 3])
    assert set_solver.is_set(cards, [2, 3, 4])


def test_find_sets():
    """Test solver (Exercise 3b)."""
    cards = numpy.array([[1,1,1,2,0],
                         [0,1,2,2,2],
                         [0,1,2,2,2],
                         [0,1,2,2,2]])

    set_indices = set_solver.find_sets(cards)
    assert len(set_indices) == 2
    assert (0, 1, 2) in set_indices
    assert (2, 3, 4) in set_indices
