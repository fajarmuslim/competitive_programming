from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for item1 in nums1: 
            search = False
            temp_res = -1
            for i in range(len(nums2)):
                if item1 == nums2[i]:
                    search = True
                
                if search==True and nums2[i]>item1:
                    temp_res = nums2[i]
                    break
            
            res.append(temp_res)
        
        return res
                    
                    