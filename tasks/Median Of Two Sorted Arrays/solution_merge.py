import math
from typing import List


def merge(nums1: List[int], nums2: List[int]) -> List[int]:
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    else:
        if i != len(nums1):
            result.extend(nums1[i:])

        if j != len(nums2):
            result.extend(nums2[j:])
    return result


def solution(nums1: List[int], nums2: List[int]) -> float:
    merged_array = merge(nums1, nums2)

    center = (len(merged_array) - 1) / 2
    median = .0

    if len(merged_array) % 2 == 0:
        center = int(math.floor(center))
        el1 = merged_array[center]
        el2 = merged_array[center + 1]
        median = (el1 + el2) / 2
    else:
        median = merged_array[int(center)]

    return median
