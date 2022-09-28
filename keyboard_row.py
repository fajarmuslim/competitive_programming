from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def check_in(word):
            rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
            res = []
            
            for row in rows:
                valid = True
                for char in word.lower():
                    if char not in row:
                        valid = False
                        break
                if valid:
                    res.append(word)
            
            return res
        
        result = []
        for word in words:
            for item in check_in(word):
                result.append(item)
            
        return result