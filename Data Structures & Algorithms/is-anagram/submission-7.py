class Solution:
    def _get_char_count_map(self, string):
        char_map = {}
        for char in string:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1 

        return char_map

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
         
        return self._get_char_count_map(s) == self._get_char_count_map(t)
        