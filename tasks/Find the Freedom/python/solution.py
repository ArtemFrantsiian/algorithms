import unittest


def solution(n, k, l):
    l.sort()
    res = set()
    for i in range(n):
        if l[i] % k != 0 or l[i] / k not in res:
            res.add(l[i])

    return len(res)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution(6, 2, [2, 3, 6, 5, 4, 10]), 3)

    def test_2(self):
        self.assertEqual(solution(10, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 6)

    def test_3(self):
        self.assertEqual(solution(1, 1, [1]), 1)

    def test_4(self):
        self.assertEqual(solution(6, 2, [6, 3, 2, 5, 4, 10]), 3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
