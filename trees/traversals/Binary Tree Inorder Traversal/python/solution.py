import unittest
from typing import List


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Node) -> List[int]:
    if not root:
        return []
    result = []

    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited:
                stack.extend([
                    (node.right, False),
                    (node, True),
                    (node.left, False)
                ])
            else:
                result.append(node.val)

    return result


class Test(unittest.TestCase):
    def test1(self):
        node = Node(1, right=Node(2, left=Node(3)))
        self.assertEqual(inorder(node), [1, 3, 2])

    def test2(self):
        node = Node(1, left=Node(2), right=Node(3, left=Node(4)))
        self.assertEqual(inorder(node), [2, 1, 4, 3])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
