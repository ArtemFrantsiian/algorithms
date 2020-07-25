import unittest


def binary_search(values, v):
    left = 0
    right = len(values) - 1

    while left <= right:
        m = (left + right) // 2

        if values[m] < v:
            left = m + 1
        elif values[m] > v:
            right = m - 1
        else:
            return m

    return None


def solution(s, x):
    s = list(s)
    for i, v in enumerate(s):
        f = x - v

        if f < 0:
            return False

        if binary_search(s[:i] + s[i + 1:], f) is None:
            return False

        return True


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution({1, 2, 3, 4, 5, 6, 7}, 3), True)

    def test_2(self):
        self.assertEqual(solution({26, 31, 41, 58, 59}, 82), False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
