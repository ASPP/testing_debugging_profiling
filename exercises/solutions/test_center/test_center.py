from py.test import raises


def test_center_default():
    # cases are (arguments, [possible results of centering])
    cases = [(('a', 5),    ['  a  ']),
             (('a', 4),    [' a  ', '  a ']),
             (('[]', 5),   [' []  ', '  [] ']),
             (('[]', 4),   [' [] ']),
             (('test', 2), ['test']),
             (('', 3),     ['   ']),
             ((' a', 5),   ['  a  ', '   a '])]

    # test all cases
    for (str_, width), expected in cases:
        output = str_.center(width)

        assert len(output) == max(width, len(str_))
        assert output in expected


def test_center_fillchar():
    cases = [(('a', 5), ['**a**']),
             (('a', 4), ['*a**', '**a*'])]

    # test all cases
    for fillchar in ['#', '5', ' ']:
        for (str_, width), expected in cases:
            output = str_.center(width, fillchar)

            assert len(output) == max(width, len(str_))
            assert output.replace(fillchar, '*') in expected


def test_errors():
    with raises(TypeError):
        'a'.center('')

    with raises(TypeError):
        'a'.center('*#')
