from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (nums[i] == nums[j]) & (i < j):
                    res += 1
        return res