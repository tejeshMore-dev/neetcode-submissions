class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f_map = {}

        for char in s:
            f_map[char] = f_map.get(char, 0) +  1
        
        for char in t:
            if char not in f_map:
                return False

            f_map[char] -= 1

            if f_map[char] < 0:
                return False 
            
        return True