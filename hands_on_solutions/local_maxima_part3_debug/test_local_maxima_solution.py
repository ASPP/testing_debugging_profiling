import numpy as np
import pytest

from local_maxima_solution import find_maxima


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


# the tests below here fail, can you get them to pass?


def test_find_maxima_correct_order():
    values = [2, 1, 5, 1, 9]
    expected = [0, 2, 4]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_one_value():
    values = [1]
    expected = [0]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_long_plateau():
    values = [1, 2, 2, 2, 2, 2, 1, 8, 0]
    expected = [3, 7]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau_at_end():
    values = [1, 2, 2]
    expected = [1]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau_at_start():
    values = [1, 1, 0, 0]
    expected = [0]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_all_same_values():
    values = [1, 1]
    expected = [0]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_letters():
    values = ["T", "e", "s", "t", "s", "!"]
    expected = [0, 3]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_new_inputs_to_make_current_function_fail():
    # should you actually be done with all tests, then you can think of other cases where the current function fails
    # and write tests for them and fix them
    assert True
