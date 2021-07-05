from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        max_num_g = 0
        for idx in range(len(nums) - 1):
            if nums[idx] == 1:
                max_num += 1
            elif nums[idx] == 0:
                if max_num > max_num_g:
                    max_num_g = max_num
                max_num = 0

        if (len(nums) - 1) >= 0:
            if nums[len(nums) - 1] == 1:
                max_num += 1
                if max_num > max_num_g:
                    max_num_g = max_num
            elif nums[len(nums) - 1] == 0:
                if max_num > max_num_g:
                    max_num_g = max_num
                max_num = 0

        return max_num_g
