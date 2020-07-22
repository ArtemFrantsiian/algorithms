import unittest
import numpy as np


def s(a, b):
    n = len(a)
    c = np.empty((n, n), dtype=int)

    if n == 1:
        c[0][0] = a[0][0] * b[0][0]
    else:
        mid = n // 2

        a11 = a[:mid, :mid]
        a12 = a[:mid, mid:]
        a21 = a[mid:, :mid]
        a22 = a[mid:, mid:]

        b11 = b[:mid, :mid]
        b12 = b[:mid, mid:]
        b21 = b[mid:, :mid]
        b22 = b[mid:, mid:]

        m1 = s(a11, b11) + s(a11, b22) + s(a22, b11) + s(a22, b22)
        m2 = s(a21, b11) + s(a22, b11)
        m3 = s(a11, b12) - s(a11, b22)
        m4 = s(a22, b21) - s(a22, b11)
        m5 = s(a11, b22) + s(a12, b22)
        m6 = s(a21, b11) + s(a21, b12) - s(a11, b11) - s(a11, b12)
        m7 = s(a12, b21) + s(a12, b22) - s(a22, b21) - s(a22, b22)

        c11 = m1 + m4 - m5 + m7
        c12 = m3 + m5
        c21 = m2 + m4
        c22 = m1 - m2 + m3 + m6

        c1 = np.concatenate((c11, c12), axis=1)
        c2 = np.concatenate((c21, c22), axis=1)
        c = np.concatenate((c1, c2))

    return c


def solution(a, b):
    a = np.array(a)
    b = np.array(b)

    n = len(a)
    is_trailing = False

    if n % 2 != 0:
        zeros = np.zeros((n + 1, n + 1), dtype=int)

        az = zeros.copy()
        az[:-1, :-1] = a
        bz = zeros
        bz[:-1, :-1] = b

        a = az
        b = bz

        is_trailing = True

    res = s(a, b)

    if is_trailing:
        res = np.delete(res, n, axis=0)
        res = np.delete(res, n, axis=1)

    return res.tolist()


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([
            [1, 3],
            [7, 5]
        ], [
            [6, 8],
            [4, 2]
        ]), [
            [18, 14],
            [62, 66]
        ])

    def test_2(self):
        self.assertEqual(solution([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [
            [9, 6, 3],
            [8, 5, 2],
            [7, 4, 1]
        ]), [
            [46, 28, 10],
            [118, 73, 28],
            [190, 118, 46]
        ])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
