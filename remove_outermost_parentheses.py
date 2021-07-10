from collections import deque


class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        stack = deque()
        idx_outer = []

        for i in range(len(S)):
            if not stack:
                stack.append(S[i])
                idx_outer.append(i)
                continue
            # check peek
            elif (S[i] == ")") & (stack[-1] == "("):
                stack.pop()
                if not stack:
                    idx_outer.append(i)
            else:
                stack.append(S[i])

        res = ""
        for i in range(len(S)):
            if i not in idx_outer:
                res += S[i]

        return res