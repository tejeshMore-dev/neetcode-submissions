class Solution:
    # def _get_char_count_map(self, string):
    #     char_map = {}
    #     for char in string:
    #         if char in char_map:
    #             char_map[char] += 1
    #         else:
    #             char_map[char] = 1 

    #     return char_map

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
         
    #     return self._get_char_count_map(s) == self._get_char_count_map(t)
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
         
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        for char in t:
            if char not in char_map:
                return False
            
            char_map[char] -= 1

            if char_map[char] < 0:
                return False
    
        return True