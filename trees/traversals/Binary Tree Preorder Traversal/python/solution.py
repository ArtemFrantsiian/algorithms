import unittest
from typing import List


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: Node) -> List[int]:
    stack = [root]

    result = []
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return result


class Test(unittest.TestCase):
    def test1(self):
        node = Node(1, right=Node(2, left=Node(3)))
        self.assertEqual(preorder(node), [1, 2, 3])

    def test2(self):
        node = Node(1, left=Node(2), right=Node(3, left=Node(4)))
        self.assertEqual(preorder(node), [1, 2, 3, 4])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
