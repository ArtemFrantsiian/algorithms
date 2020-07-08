import unittest


def insertion_sort(unsorted_values):
    for i in range(1, len(unsorted_values)):
        key = unsorted_values[i]
        j = i - 1

        while j >= 0 and unsorted_values[j] > key:
            unsorted_values[j + 1] = unsorted_values[j]
            j = j - 1

        unsorted_values[j + 1] = key

    return unsorted_values


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(insertion_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
