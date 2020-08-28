import unittest


def _rbs(values, l, r, v):
    m = (l + r) // 2
    if values[m] == v:
        return m

    if r < 1:
        return None

    if values[m] > v:
        return _rbs(values, l, m - 1, v)

    return _rbs(values, m + 1, r, v)


def r_binary_search(values, v):
    return _rbs(values, 0, len(values) - 1, v)


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(r_binary_search([1, 2, 3, 4, 5, 6, 7], 1), 0)

    def test_2(self):
        self.assertEqual(r_binary_search([26, 31, 41, 41, 58, 59], 30), None)

    def test_3(self):
        self.assertEqual(r_binary_search([26, 31, 41, 41, 58, 59], 41), 2)

    def test_4(self):
        self.assertEqual(r_binary_search([26, 31, 41, 41, 58, 59], 59), 5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
