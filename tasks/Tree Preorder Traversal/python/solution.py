import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: Node) -> List[int]:
    stack = [root]

    result = []
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])

    return result


class Test(unittest.TestCase):
    def test1(self):
        node = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        self.assertEqual(preorder(node), [1, 3, 5, 6, 2, 4])

    def test2(self):
        node = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
        self.assertEqual(preorder(node), [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
