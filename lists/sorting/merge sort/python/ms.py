import unittest


def merge(unsorted_values, left, right):
    i = j = 0

    for k in range(0, len(unsorted_values)):
        if i == len(left):
            unsorted_values[k] = right[j]
            j = j + 1
            continue

        if j == len(right):
            unsorted_values[k] = left[i]
            i = i + 1
            continue

        if left[i] <= right[j]:
            unsorted_values[k] = left[i]
            i = i + 1
        else:
            unsorted_values[k] = right[j]
            j = j + 1


def merge_sort(unsorted_values):
    p = 1
    r = len(unsorted_values)
    if p >= r:
        return unsorted_values

    q = (p + r) / 2
    left = merge_sort(unsorted_values[:q])
    right = merge_sort(unsorted_values[q:])
    merge(unsorted_values, left, right)
    return unsorted_values


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(merge_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(merge_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
