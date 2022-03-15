from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for idx in range(len(prices)-1, 0, -1):
            if prices[idx] - prices[idx-1] > 0:
                result = result + prices[idx] - prices[idx-1]
        
        return result