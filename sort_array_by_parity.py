from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        found_left, found_right = False, False
        val_left, val_right = 0, 0

        while l < r:
            if found_left == False:
                if nums[l] % 2 != 0:
                    found_left = True
                    val_left = nums[l]
                else:
                    l += 1

            if found_right == False:
                if nums[r] % 2 != 1:
                    found_right = True
                    val_right = nums[r]
                else:
                    r -= 1

            if found_left and found_right:
                nums[l], nums[r] = val_right, val_left
                found_left, found_right = False, False

        return nums