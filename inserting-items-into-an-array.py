from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        adding_in_prev_idx = False
        len_arr = len(arr)
        for idx in range(len_arr):
            if adding_in_prev_idx:
                adding_in_prev_idx = False
                continue

            if arr[idx] == 0:
                arr.insert(idx, 0)
                arr.pop(len(arr) - 1)
                adding_in_prev_idx = True