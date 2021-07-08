from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                continue

            for j in range(len(arr)):
                if i == j:
                    continue
                if arr[i] == 2 * arr[j]:
                    return True