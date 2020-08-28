import unittest


def bubble_sort(uv):
    n = len(uv)
    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if uv[j] < uv[j - 1]:
                uv[j - 1], uv[j] = uv[j], uv[j - 1]

    return uv


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(bubble_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(bubble_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
