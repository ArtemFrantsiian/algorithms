const permute = function(nums) {
    const result = [];

    const backtracking = (combination) => {
        if (combination.length === nums.length) {
            result.push(combination);
            return;
        }

        for (const el of nums) {
            if (combination.includes(el)) {
                continue;
            }

            backtracking([...combination, el]);
        }
    }

    backtracking([]);
    return result;
};