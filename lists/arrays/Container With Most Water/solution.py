class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        if not height:
            return max_area

        n = len(height)
        l = 0
        r = n - 1

        while r > l:
            a = min(height[l], height[r])
            b = r - l
            area = a * b
            max_area = max(max_area, area)
            if a == height[l]:
                l += 1
            else:
                r -= 1

        return max_area