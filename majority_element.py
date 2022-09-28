from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        
        res_reversed = {v:k for k,v in res.items()}

        return res_reversed[max(res_reversed.keys())]