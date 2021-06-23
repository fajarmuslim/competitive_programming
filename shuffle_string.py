from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        dict_p = {}
        res = ""
        for i in range(len(s)):
            dict_p[indices[i]] = s[i]

        for i in range(len(s)):
            res += dict_p[i]

        return res