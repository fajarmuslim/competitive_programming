class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_match = 0
        count_L = 0
        count_R = 0

        for char in s:
            if char == "L":
                count_L += 1
            if char == "R":
                count_R += 1

            if (count_L == count_R) & (count_L != 0):
                count_match += 1
                count_L = 0
                count_R = 0
        return count_match