from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        res = []
        count = 0
        for item in nums:
            if item != val:
                res.append(item)
                count += 1

        for idx in range(count):
            nums[idx] = res[idx]

        return count