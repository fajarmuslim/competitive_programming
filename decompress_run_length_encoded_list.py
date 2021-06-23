from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        idx = 0
        while idx < len(nums):
            freq = nums[idx]
            val = nums[idx + 1]

            res += [val for j in range(freq)]

            idx += 2

        return res
