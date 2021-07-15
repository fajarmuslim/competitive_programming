from typing import List


class Solution:
    def helper(self, idx, s: List[str], len_s_per_2: int):
        if idx == len_s_per_2:
            return s
        else:
            s[idx], s[len(s) - 1 - idx] = s[len(s) - 1 - idx], s[idx]
            return self.helper(idx + 1, s, len_s_per_2)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s_per_2 = len(s) // 2
        return self.helper(0, s, len_s_per_2)