import numpy as np
import pytest

from local_maxima import find_maxima


def test_find_maxima():
    values = [1, 3, -2, 0, 2, 1]
    expected = [1, 4]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_edges():
    values = [4, 2, 1, 0, 1, 5]
    expected = [0, 5]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_empty():
    values = []
    expected = []
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau():
    values = [1, 2, 2, 1]
    expected = [1]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_not_a_plateau():
    values = [1, 2, 2, 3, 1]
    expected = [3]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau_at_end():
    values = [1, 2, 2]
    expected = [1]
    maxima = find_maxima(values)
    assert maxima == expected


# these are the new tests


def test_find_maxima_one_value():
    values = [1]
    expected = [0]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau_at_start():
    values = [2, 2, 1, 0]
    expected = [0]
    maxima = find_maxima(values)
    assert maxima == expected
