from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            unique_element = nums[0]
            idx = 0
            for i in range(1, len(nums)):
                if nums[i] != unique_element:
                    idx += 1
                    nums[idx] = nums[i]
                    unique_element = nums[i]
            return idx + 1