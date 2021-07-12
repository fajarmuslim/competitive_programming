from typing import Counter, List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights.copy()
        heights.sort()

        # print(heights)
        count = 0
        for idx in range(len(heights)):
            if temp[idx] != heights[idx]:
                count += 1

        return count


s = Solution()
s.heightChecker([1, 1, 4, 2, 1, 3])
