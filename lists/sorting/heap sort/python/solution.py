import unittest


def left(i):
    return i << 1  # 2 * i


def right(i):
    x = i << 1
    m = 1

    while x & m:
        x = x ^ m
        m <<= 1

    x = x ^ m
    return x  # 2 * i + 1


def max_heapify(t, i, heap_size):
    l = left(i)
    r = right(i)

    largest = i
    if l <= heap_size and t[l] > t[largest]:
        largest = l
    if r <= heap_size and t[r] > t[largest]:
        largest = r

    if largest != i:
        t[i], t[largest] = t[largest], t[i]
        max_heapify(t, largest, heap_size)


def build_max_heap(t, heap_size):
    for i in range(len(t) // 2, -1, -1):
        max_heapify(t, i, heap_size)


def heap_sort(t):
    heap_size = len(t) - 1
    build_max_heap(t, heap_size)
    for i in range(len(t) - 1, 0, -1):
        t[0], t[i] = t[i], t[0]
        heap_size = heap_size - 1
        max_heapify(t, 0, heap_size)
    return t


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(heap_sort([5, 3, 2, 7, 6, 4, 1]), [1, 2, 3, 4, 5, 6, 7])

    def test_2(self):
        self.assertEqual(heap_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
