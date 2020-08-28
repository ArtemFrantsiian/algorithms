import unittest
import random


def random_search(values, v):
    cv = set(values)

    while bool(cv):
        ri = random.randrange(0, len(values))

        if values[ri] == v:
            return ri
        else:
            cv.discard(values[ri])

    return None


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(random_search([1, 2, 3, 4, 5, 6, 7], 1), 0)

    def test_2(self):
        self.assertEqual(random_search([26, 31, 41, 41, 58, 59], 30), None)

    def test_3(self):
        self.assertEqual(random_search([26, 31, 41, 41, 58, 59], 59), 5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
