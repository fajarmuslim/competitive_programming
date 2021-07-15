from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for curr_idx in range(len(nums)):
            idx = abs(nums[curr_idx])

            if nums[idx - 1] > 0:
                nums[idx - 1] = -1 * nums[idx - 1]

        res = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                res.append(idx + 1)

        return res