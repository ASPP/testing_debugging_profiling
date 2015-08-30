import unittest


class TestStringLen(unittest.TestCase):
    def test_len(self):
        # Given
        # Each test case is a tuple of (input, expected_len)
        cases = [('hallo', 5),
                 ('', 0),
                 ('!*#$@#', 5)]

        for string, expected_len in cases:
            # When
            result = len(string)
            # Then
            self.assertEqual(result, expected_len)


if __name__ == '__main__':
    unittest.main()
