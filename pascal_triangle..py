from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            res = [[1]]
        if numRows > 1:
            res = [[1], [1,1]]
        
        for i in range(2,numRows):
            temp = [1]
            
            for j in range(len(res[i-1])-1):
                temp.append(res[i-1][j] + res[i-1][j+1])
            temp.append(1)
        
            res.append(temp)
        
        return res