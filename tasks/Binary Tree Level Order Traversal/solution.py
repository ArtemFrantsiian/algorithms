def solution(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while len(queue) > 0:

        level = []

        for _ in range(len(queue)):
            vertex = queue.pop(0)  # ToDo: Check what is the fastest way to work with FIFO deque or list via plot
            level.append(vertex.val)

            if vertex.left:
                queue.append(vertex.left)

            if vertex.right:
                queue.append(vertex.right)

        result.append(level)

    return result

