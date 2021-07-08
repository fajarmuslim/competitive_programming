from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        candidate_breaking = False
        candidate_peak_idx = 0

        if len(arr) < 3:
            return candidate_breaking
        else:
            for i in range(len(arr) - 1):
                if arr[i + 1] > arr[i]:
                    continue
                else:
                    candidate_breaking = True
                    candidate_peak_idx = i
                    break

            if candidate_peak_idx == 0:
                return False
            for j in range(candidate_peak_idx, len(arr) - 1):
                if arr[j + 1] < arr[j]:
                    continue
                else:
                    candidate_breaking = False
                    break

        return candidate_breaking
