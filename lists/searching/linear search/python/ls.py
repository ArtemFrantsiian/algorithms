import unittest


def linear_search(values, v):
    position = None
    for i in range(1, len(values)):
        if i == v:
            position = values.index(i)
            break

    return position


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(linear_search([5, 3, 2, 7, 6, 4, 1], 3), 1)

    def test_2(self):
        self.assertEqual(linear_search([31, 41, 59, 26, 41, 58], 30), None)

    def test_3(self):
        self.assertEqual(linear_search([5, 3, 2, 7, 3, 4, 1], 3), 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
