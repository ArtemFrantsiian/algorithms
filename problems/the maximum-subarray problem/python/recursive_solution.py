import unittest


def find_crossing_subarray(arr, l, m, h):
    ml = 0
    mr = 0

    ls = -float('Inf')
    sum = 0
    for i in range(m, l, -1):
        sum += arr[i]
        if sum > ls:
            ls = sum
            ml = i

    rs = -float('Inf')
    sum = 0
    for i in range(m + 1, h):
        sum += arr[i]
        if sum > rs:
            rs = sum
            mr = i

    return ml, mr, ls + rs


def find_max_subarray(arr, l, h):
    if l == h:
        return l, h, arr[l]

    mid = (l + h) // 2
    ll, rl, sl = find_max_subarray(arr, l, mid)
    lr, rr, sr = find_max_subarray(arr, mid + 1, h)
    lc, rc, sc = find_crossing_subarray(arr, l, mid, h)

    if sl >= sr and sl >= sc:
        return ll, rl, sl
    elif sr >= sl and sr >= sc:
        return lr, rr, sr
    else:
        return lc, rc, sc


def solution(arr):
    left, right, sum = find_max_subarray(arr, 0, len(arr) - 1)
    return arr[left:right + 1], sum


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([2, -6, 2, -1]), ([2], 2))

    def test_2(self):
        self.assertEqual(
            solution([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]),
            ([18, 20, -7, 12], 43)
        )


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
