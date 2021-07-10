class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        res = 0
        right = len(mat) - 1
        
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][right]
            right -= 1
        
        
         
        if len(mat) % 2 == 1:
            half = int(len(mat)/2)
            return res - mat[half][half]
        else:
            return res
            
        