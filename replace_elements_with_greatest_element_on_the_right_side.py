from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = arr[len(arr) - 1]
        last_element = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= max_so_far:
                arr[i] = max_so_far
            else:
                max_so_far = arr[i]

        arr.insert(len(arr) - 1, last_element)
        arr = arr[1:]
        arr[len(arr) - 1] = -1
        return arr
