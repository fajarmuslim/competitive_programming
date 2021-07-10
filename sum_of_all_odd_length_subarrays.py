from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0

        for i in range(1, len(arr) + 1, 2):
            idx = 0
            inc = 0

            while (inc + i) < (len(arr) + 1):
                for j in range(idx + inc, i + inc):
                    res += arr[j]

                inc += 1

        return res