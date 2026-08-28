from local_maxima import find_maxima


def test_find_maxima():
    values = [1, 3, -2, 0, 2, 1]
    expected = [1, 4]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_edges():
    values = [4, 2, 1, 3, 1, 5]
    expected = [0, 3, 5]
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
