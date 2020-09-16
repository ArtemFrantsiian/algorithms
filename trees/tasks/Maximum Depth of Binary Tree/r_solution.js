const traverse = (r, level) => {
    if (r === null) {
        return level;
    }

    level += 1;

    const left = traverse(r.left, level);
    const right = traverse(r.right, level);

    return Math.max(left, right);
};

const maxDepth = function(root) {
    return traverse(root, 0);
};