class Solution:            
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            res = [1]
            prev_row = self.getRow(rowIndex-1)
            
            for i in range(rowIndex-1):
                res.append(prev_row[i] + prev_row[i+1])
            
            res.append(1)
    
        return res 