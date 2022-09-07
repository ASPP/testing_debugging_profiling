from local_maxima import local_maxima


def test_local_maxima():
    values = [1, 3, -2, 0, 2, 1]
    expected = [1, 4]
    maxima = local_maxima(values)
    assert maxima == expected


def test_local_maxima_negative():
    values = [-1, -1, 0, -1]
    expected = [2]
    maxima = local_maxima(values)
    assert maxima == expected


def test_local_maxima_edges():
    values = [4, 2, 1, 3, 1, 5]
    expected = [0, 3, 5]
    maxima = local_maxima(values)
    assert maxima == expected


def test_local_maxima_plateau():
    values = [1, 2, 2, 1]
    expected = [1]
    maxima = local_maxima(values)
    assert maxima == expected


def test_local_maxima_not_a_plateau():
    values = [1, 2, 2, 3, 1]
    expected = [3]
    maxima = local_maxima(values)
    assert maxima == expected
