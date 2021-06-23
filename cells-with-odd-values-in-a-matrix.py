import numpy as np

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        init_mat = [[0 for i in range(n)] for j in range(m)]
        
        rows = []
        columns = []
        
        for item in indices:
            rows.append(item[0])
            columns.append(item[1])
        
        
        for row in rows:
            init_mat[row] = [item + 1 for item in init_mat[row]]
        
        init_mat_T = np.array(init_mat).T.tolist()
        
        for column in columns:
            init_mat_T[column] = [item + 1 for item in init_mat_T[column]]
            
        final_mat =  np.array(init_mat_T).T.tolist()
        
        res = 0
        for row in final_mat:
            for item in row:
                if item % 2 == 1:
                    res += 1
        return res