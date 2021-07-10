class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitted_sentence = s.split(' ')
        return ' '.join(splitted_sentence[:k])