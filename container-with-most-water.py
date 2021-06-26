from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxa = 0
        l, r = 0, (len(height) - 1)

        while l < r:
            max_temp = (r - l) * min(height[l], height[r])
            if max_temp > maxa:
                maxa = max_temp

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return maxa