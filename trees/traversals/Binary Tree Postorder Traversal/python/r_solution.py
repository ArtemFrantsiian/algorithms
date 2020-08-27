import unittest
from typing import List


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_recursion(root: Node) -> List[int]:
    if not root:
        return []

    result = []
    result.extend(postorder_recursion(root.left))
    result.extend(postorder_recursion(root.right))
    result.append(root.val)

    return result


class Test(unittest.TestCase):
    def test1(self):
        node = Node(1, right=Node(2, left=Node(3)))
        self.assertEqual(postorder_recursion(node), [3, 2, 1])

    def test2(self):
        node = Node(1, left=Node(2), right=Node(3, left=Node(4)))
        self.assertEqual(postorder_recursion(node), [2, 4, 3, 1])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
