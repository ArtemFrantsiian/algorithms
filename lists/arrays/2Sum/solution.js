const assert = require('assert').strict;

const twoSum = function(nums, target) {
    const ht = new Map();
    const indexes = [];

    for (let i = 0; i < nums.length; i++) {
        const val = target - nums[i]
        if (ht.has(val)) {
            return [ht.get(val), i]
        }

        ht.set(nums[i], i)
    }
};

assert.deepEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
assert.deepEqual(twoSum([3, 2, 4], 6), [1, 2]);
assert.deepEqual(twoSum([3, 3], 6), [0, 1]);