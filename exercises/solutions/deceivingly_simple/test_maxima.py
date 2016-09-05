from py.test import raises

from maxima import find_maxima


def test_last_element():
    x = [1, 2]
    idx = find_maxima(x)
    assert idx == [1]


def test_first_element():
    x = [3, 1, 4]
    idx = find_maxima(x)
    assert idx == [0, 2]


def test_equality():
    case_res = [([1, 2, 2, 1, 1], [2]),
                ([1, 2, 2, 3, 1], [3]),
                ([1, 3, 2, 2, 1], [1]),
                ([3, 2, 2, 2, 3], [0, 4])]
    for x, desired in case_res:
        idx = find_maxima(x)
        assert idx == desired


def test_check_input():
    with raises(ValueError):
        find_maxima(2)

