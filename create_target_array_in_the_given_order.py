from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for idx, num in zip(index, nums):
            if idx > len(res):
                res.append(num)
            else:
                left = res[:idx]
                right = res[idx:]

                res = left + [num] + right

        return res