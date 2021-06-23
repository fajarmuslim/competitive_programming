from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            ruleIdx = 0
            if ruleKey == "color":
                ruleIdx = 1
            elif ruleKey == "name":
                ruleIdx = 2

            if item[ruleIdx] == ruleValue:
                count += 1

        return count