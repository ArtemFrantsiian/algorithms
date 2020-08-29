import unittest
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root: Node) -> List[int]:
    if not root:
        return []

    result = []

    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()

        if node:
            if not visited:
                stack.append((node, True))
                if node.children:
                    stack.extend([(i, False) for i in node.children[::-1]])
            else:
                result.append(node.val)

    return result


class Test(unittest.TestCase):
    def test1(self):
        node = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        self.assertEqual(postorder(node), [5, 6, 3, 2, 4, 1])

    def test2(self):
        node = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
        self.assertEqual(postorder(node), [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
