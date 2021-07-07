from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        res = []
        count = 0
        for idx in range(len(nums) - 1):
            if nums[idx] != nums[idx + 1]:
                res.append(nums[idx])
                count += 1

        # handle last element of nums
        # case when res has been filled
        if len(nums) != 0 and len(res) != 0:
            if nums[len(nums) - 1] != res[len(res) - 1]:
                res.append(nums[len(nums) - 1])
                count += 1

        # case when res doesn't filled yet
        if len(nums) != 0 and len(res) == 0:
            res.append(nums[len(nums) - 1])
            count += 1

        for idx in range(count):
            nums[idx] = res[idx]

        return count