class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_frequency = {}
        for char in s:
            s_char_frequency[char] = s_char_frequency.get(char, 0) + 1
    
        t_char_frequency = {}
        for char in t:
            t_char_frequency[char] = t_char_frequency.get(char, 0) + 1

        return s_char_frequency == t_char_frequency