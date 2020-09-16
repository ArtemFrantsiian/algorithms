const maxDepth = function(root) {
    const queue = [[root, 0]];
    let max_level = 0;
    while (queue.length) {
        const [el, level] = queue.shift();

        if (el === null) {
            max_level = Math.max(max_level, level);
            continue;
        }

        queue.push([el.left, level + 1]);
        queue.push([el.right, level + 1]);
    }
    return max_level;
};
