from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(sum([item < num for item in nums]))
        return res