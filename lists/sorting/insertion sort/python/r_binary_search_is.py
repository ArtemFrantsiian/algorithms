import unittest


def _rbs(values, left, right, v):
    m = (left + right) // 2
    if values[m] == v:
        return m

    if left == right:
        if values[left] > v:
            return left
        else:
            return left + 1

    if left > right:
        return left

    if values[m] > v:
        return _rbs(values, left, m - 1, v)

    return _rbs(values, m + 1, right, v)


def recursive_binary_search(values, v):
    return _rbs(values, 0, len(values) - 1, v)


def recursive_binary_search_insertion_sort(unsorted_values):
    for i in range(1, len(unsorted_values)):
        key = unsorted_values[i]
        ii = recursive_binary_search(unsorted_values[:i], key)
        unsorted_values = unsorted_values[:ii] + [key] + unsorted_values[ii:i] + unsorted_values[i + 1:]
    return unsorted_values


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(recursive_binary_search_insertion_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(recursive_binary_search_insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
