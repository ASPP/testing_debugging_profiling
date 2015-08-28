import unittest


class TestCenter(unittest.TestCase):

    def test_center_default(self):
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

            self.assertEqual(len(output), max(width, len(str_)))
            self.assertIn(output, expected)

    def test_center_fillchar(self):
        cases = [(('a', 5), ['**a**']),
                 (('a', 4), ['*a**', '**a*'])]

        # test all cases
        for fillchar in ['#', '5', ' ']:
            for (str_, width), expected in cases:
                output = str_.center(width, fillchar)
                
                self.assertEqual(len(output), max(width, len(str_)))
                self.assertIn(output.replace(fillchar, '*'), expected)

    def test_errors(self):
        with self.assertRaises(TypeError):
            'a'.center('')

        with self.assertRaises(TypeError):
            'a'.center('*#')


if __name__ == '__main__':
    unittest.main()
