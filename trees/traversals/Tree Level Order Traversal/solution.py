from collections import deque


def solution(root):
    if not root:
        return []

    queue = deque([root])

    result = []

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)

        result.append(level)

    return result

