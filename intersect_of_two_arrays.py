from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        nums2_dict = {}
        for num1 in nums1:
            if num1 in nums1_dict:
                nums1_dict[num1] += 1
            else:
                nums1_dict[num1] = 1
                
        for num2 in nums2:
            if num2 in nums2_dict:
                nums2_dict[num2] += 1
            else:
                nums2_dict[num2] = 1
        
        res_dict = {}
        for key1, value1 in nums1_dict.items():
            if key1 in nums2_dict:
                res_dict[key1] = value1 if value1 < nums2_dict[key1] else nums2_dict[key1]
        
        res = []
        for key, value in res_dict.items():
            for i in range(value):
                res.append(key)
        
        return res