class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n < 1:
            return nums1

        for i in range(m + n):
            if not nums2:
                break

            if nums1[i] > nums2[0]:
                nums1.insert(i, nums2.pop(0))
                nums1.pop()

        if len(nums2):
            nums1[-len(nums2):] = nums2
