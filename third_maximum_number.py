from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = float("-inf")
        second_max = float("-inf")
        third_max = float("-inf")

        for item in nums:
            if item > first_max:
                third_max = second_max
                second_max = first_max
                first_max = item
            elif item > second_max and item != first_max:
                third_max = second_max
                second_max = item
            elif item > third_max and item != second_max and item != first_max:
                third_max = item

        if third_max == float("-inf"):
            return first_max
        else:
            return third_max