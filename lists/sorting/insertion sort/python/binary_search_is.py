import unittest


def binary_search_insertion_sort(unsorted_values):
    for i in range(1, len(unsorted_values)):
        key = unsorted_values[i]
        ii = None
        left = 0
        right = i - 1

        while left <= right:
            m = (left + right) // 2

            if unsorted_values[m] == key:
                ii = m
                break

            if unsorted_values[m] < key:
                left = m + 1
            elif unsorted_values[m] > key:
                right = m - 1
            else:
                ii = m
                break

            if left > right:
                ii = left
                break

            if left == right:
                if unsorted_values[left] > key:
                    ii = left
                else:
                    ii = left + 1
                break

        unsorted_values = unsorted_values[:ii] + [key] + unsorted_values[ii:i] + unsorted_values[i + 1:]
    return unsorted_values


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(binary_search_insertion_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(binary_search_insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
