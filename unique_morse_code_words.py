from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        print(ord("a"))
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        diff_word = set()
        for word in words:
            string_in_morse = "".join([morse[ord(char) - 97] for char in word])
            diff_word.add(string_in_morse)

        return len(diff_word)