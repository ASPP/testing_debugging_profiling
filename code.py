"""
This is code that is copy-and-pasted in the slides.
"""


def test_arithmetic():
    assert 1 == 1
    assert 2 * 3 == 6

def test_len_list():
    lst = ['a', 'b', 'c']
    assert len(lst) == 3

def test_various():
    assert 'Hi'.islower()
    assert 2 + 1 == 3
    assert [2] + [1] == [2, 1]
    assert 'a' + 'b' != 'ab'


def test_1_and_2():
    assert 1 + 2 == 3

def test_1_and_2_float():
    assert 1.1 + 2.2 == 3.3


from math import isclose

def test_floating_point_math():
    assert isclose(1.1 + 2.2, 3.3)

def test_floating_point_math2():
    assert isclose(1.121, 1.2, abs_tol=1e-1)
    assert isclose(1.121, 1.2, abs_tol=1e-2)

def test_floating_point_math3():
    assert isclose(120.1, 121.4, rel_tol=1e-1)
    assert isclose(120.4, 121.4, rel_tol=1e-2)

import numpy

def test_numpy_equality():
    x = numpy.array([1, 1])
    y = numpy.array([2, 2])
    z = numpy.array([3, 3])
    assert x + y == z


