import unittest


def _ris(unsorted_values, n):
    if n <= 1:
        return

    _ris(unsorted_values, n - 1)

    key = unsorted_values[n - 1]
    j = n - 2
    while j >= 0 and unsorted_values[j] > key:
        unsorted_values[j + 1] = unsorted_values[j]
        j = j - 1

    unsorted_values[j + 1] = key


def recursive_insertion_sort(unsorted_values):
    if len(unsorted_values) <= 1:
        return unsorted_values

    _ris(unsorted_values, len(unsorted_values))
    return unsorted_values


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(recursive_insertion_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(recursive_insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
