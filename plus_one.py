from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        max_idx = len(digits)-1
        if digits[max_idx] != 9:
            digits[max_idx] += 1
            return digits
        else:
            temp_result = []
            carry_over = True
            for idx in range(max_idx, -1, -1):
                if carry_over:
                    if digits[idx] + 1 == 10:
                        carry_over = True
                        temp_result.append(0)
                    else:
                        temp_result.append(digits[idx] + 1)
                        carry_over = False
                
                if not carry_over:
                    break
                
                
            if temp_result[len(temp_result)-1] == 0:
                temp_result.append(1)
                
            for idx_1 in range(idx-1, -1, -1):
                temp_result.append(digits[idx_1])
            
            
            temp_result.reverse()
            return temp_result