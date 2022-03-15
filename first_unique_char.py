class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = {}
        
        for item in s:
            if item in temp:
                temp[item] += 1
            else:
                temp[item] = 1
        
        for idx, item in enumerate(s):
            if temp[item] == 1:
                return idx
        
        return -1