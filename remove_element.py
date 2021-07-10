from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # res = []
        # count = 0
        # for item in nums:
        #     if item != val:
        #         res.append(item)
        #         count += 1

        # for idx in range(count):
        #     nums[idx] = res[idx]

        # return count

        # efficient way
        write_pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_pointer] = nums[i]
                write_pointer += 1

        return write_pointer