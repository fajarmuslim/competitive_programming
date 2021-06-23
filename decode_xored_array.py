from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for item in encoded:
            first = item ^ first
            arr.append(first)

        return arr