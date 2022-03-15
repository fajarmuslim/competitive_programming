class Solution:
    def helper(self, s:str):
        s = s.lower()
        res = ""
        for item in s:
            if ((ord(item) <= ord('z')) and (ord(item) >= ord('a'))) or ((ord(item) <= ord('9')) and (ord(item) >= ord('0'))):
                res += item
        
        return res
        
    def isPalindrome(self, s: str) -> bool:
        s = self.helper(s)
        l,r = 0, len(s)-1

        while l<r:
            if s[l] != s[r] :
                return False

            l, r = l+1, r-1
            
        return True