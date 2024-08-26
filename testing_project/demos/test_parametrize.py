import pytest


def test_for_loop_simple():
    cases = [1, 2, 3]
    for a in cases:
        assert a > 0


@pytest.mark.parametrize('a', [1, 2, 3])
def test_parametrize_simple(a):
    # This test will be run 3 times, with a=1, a=2, and a=3
    assert a > 0


def test_for_loop_multiple():
    cases = [(1, 'hi', 'hi'), (2, 'no', 'nono')]
    for a, b, expected in cases:
        result = b * a
        assert result == expected


@pytest.mark.parametrize('a, b, expected', [(1, 'hi', 'hi'), (2, 'no', 'nono')])
def test_parametrize_multiple(a, b, expected):
    # This test will be run 2 times, with a=1, b='hi', expected='hi'
    # and a=2, b='no', expected='nono'
    result = b * a
    assert result == expected
