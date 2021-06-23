class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        start_half = s[:int (len(s)/2)]
        end_half = s[int (len(s)/2):]
        
        number_vowels_in_start_half = 0
        
        for item in start_half:
            if item in vowels:
                number_vowels_in_start_half += 1
        
        number_vowels_in_end_half = 0
        for item in end_half:
            if item in vowels:
                number_vowels_in_end_half += 1
        
        return number_vowels_in_start_half == number_vowels_in_end_half