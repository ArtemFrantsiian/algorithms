import unittest


def selection_sort(unsorted_values):
    for i in range(0, len(unsorted_values)):
        min_value = unsorted_values[i]
        index_of_min_value = 0
        sliced = unsorted_values[i:]

        for y in range(0, len(sliced)):
            if sliced[y] < min_value:
                min_value = sliced[y]
                index_of_min_value = y

        unsorted_values[index_of_min_value + i] = unsorted_values[i]
        unsorted_values[i] = min_value

    return unsorted_values


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(selection_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(selection_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
