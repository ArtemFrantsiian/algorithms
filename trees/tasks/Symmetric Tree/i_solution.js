var isSymmetric = function(root) {
    const q = [root, root];

    while (q.length) {
        t1 = q.shift();
        t2 = q.shift();

        if (t1 === null && t2 === null) continue;
        if (t1 === null || t2 === null) return false;
        if (t1.val != t2.val) return false;

        q.push(t1.left);
        q.push(t2.right);
        q.push(t1.right);
        q.push(t2.left);
    }

    return true;
};