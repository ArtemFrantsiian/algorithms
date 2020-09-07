from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    ht = {}

    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in ht and ht[diff] != i:
            return [i, ht[diff]]
        ht[nums[i]] = i

    return []

