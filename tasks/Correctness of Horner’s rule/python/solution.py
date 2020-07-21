import unittest


def solution(s, x):
    n = len(s)

    y = s[0]

    for i in range(1, n):
        y = s[i] + y * x
        
    return y


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([2, -6, 2, -1], 3), 5)

    def test_2(self):
        self.assertEqual(solution([2, 0, 3, 1], 2), 23)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity= 2).run(suite)
