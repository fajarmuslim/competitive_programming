from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_pointer = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[write_pointer] = nums[i]
                write_pointer += 1

        for i in range(write_pointer, len(nums)):
            nums[i] = 0
        return nums