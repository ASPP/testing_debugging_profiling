from first import times_3


def test_times_3_integer():
    value = 7
    expected = 21

    result = times_3(value)

    assert result == expected


def test_times_3_string():
    value = 'wow'
    expected = 'wowwowwow'

    result = times_3(value)

    assert result == expected


def test_times_3_list():
    value = [1]
    expected = [1, 1, 1]

    result = times_3(value)

    assert result == expected
