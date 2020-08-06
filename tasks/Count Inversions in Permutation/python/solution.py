import unittest


def merge(p, left, right):
    i = j = 0
    q = 0

    for k in range(0, len(p)):
        if i == len(left):
            p[k] = right[j]
            j = j + 1
            continue

        if j == len(right):
            p[k] = left[i]
            i = i + 1
            q += 1
            continue

        if left[i] <= right[j]:
            p[k] = left[i]
            i = i + 1
        else:
            p[k] = right[j]
            j = j + 1
            q += 1

    return q


def solution(p):
    l = 1
    r = len(p)
    q = 0
    if l >= r:
        return p, q

    m = (l + r) // 2
    left, ql = solution(p[:m])
    right, qr = solution(p[m:])
    q += ql + qr + merge(p, left, right)
    return p, q


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        # TODO: remove unpacking
        _, q = solution([2, 3, 8, 6, 1])
        self.assertEqual(q, 5)

    def test_2(self):
        _, q = solution([31, 41, 59, 26, 41, 58])
        self.assertEqual(q, 4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
