from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if (
                        (i < j)
                        & (j < k)
                        & (abs(arr[i] - arr[j]) <= a)
                        & (abs(arr[j] - arr[k]) <= b)
                        & (abs(arr[i] - arr[k]) <= c)
                    ):
                        count += 1

        return count