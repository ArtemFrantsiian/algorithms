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


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 1), 0)

    def test_2(self):
        self.assertEqual(binary_search([26, 31, 41, 41, 58, 59], 30), None)

    def test_3(self):
        self.assertEqual(binary_search([26, 31, 41, 41, 58, 59], 41), 2)

    def test_4(self):
        self.assertEqual(binary_search([26, 31, 41, 41, 58, 59], 59), 5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
