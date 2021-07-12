from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # squared number in nums
        sq_nums = []
        for item in nums:
            sq_nums.append(item * item)

        l, r = 0, len(nums) - 1

        sorted_sq_nums = []
        while (l <= r) or (r >= l):
            if sq_nums[l] >= sq_nums[r]:
                sorted_sq_nums.append(sq_nums[l])
                l += 1
            else:
                sorted_sq_nums.append(sq_nums[r])
                r -= 1

        sorted_sq_nums.reverse()

        return sorted_sq_nums