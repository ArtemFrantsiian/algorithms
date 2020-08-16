from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ToDo Improve performance: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/
def solution(preorder: List[int], inorder: List[int]) -> TreeNode or None:
    if len(preorder) == 0:
        return None

    node = TreeNode(preorder[0])
    parent = inorder.index(preorder[0])
    if len(preorder) == 1:
        return node

    node.left = solution(
        preorder[1:parent + 1],
        inorder[:parent]
    )
    node.right = solution(
        preorder[parent + 1:],
        inorder[parent + 1:]
    )
    return node
