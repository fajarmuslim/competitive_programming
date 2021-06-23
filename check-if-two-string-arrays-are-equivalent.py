from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1 = ""
        for subword in word1:
            res1 += subword

        res2 = ""
        for subword in word2:
            res2 += subword

        return res1 == res2