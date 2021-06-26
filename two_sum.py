from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_items = {}  # value: index

        for idx, item in enumerate(nums):
            diff = target - item

            if diff in prev_items:
                return [prev_items[diff], idx]
            prev_items[item] = idx