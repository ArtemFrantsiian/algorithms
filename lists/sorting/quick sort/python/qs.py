import unittest


def partition(uarr, s, f):
    pivot = uarr[f]
    i = s
    for j in range(s, f):
        if uarr[j] < pivot:
            uarr[j], uarr[i] = uarr[i], uarr[j]
            i += 1

    uarr[i], uarr[f] = uarr[f], uarr[i]
    return i


def dac(uarr, s, f):
    if s < f:
        p = partition(uarr, s, f)
        dac(uarr, s, p - 1)
        dac(uarr, p + 1, f)


def quick_sort(uarr):
    dac(uarr, 0, len(uarr) - 1)
    return uarr


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(quick_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(quick_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)