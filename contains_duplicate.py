from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_set = set()
        for num in nums:
            if num in temp_set:
                return True
            else:
                temp_set.add(num)
        
        return False
        