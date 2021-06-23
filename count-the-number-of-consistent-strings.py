from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            isConsistent = 1

            for char in word:
                if char not in allowed:
                    isConsistent = 0

            count += isConsistent

        return count