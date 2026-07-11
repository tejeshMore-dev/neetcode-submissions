from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f_map = defaultdict(int)
        
        for i, char in enumerate(s):
            f_map[s[i]] += 1
            f_map[t[i]] -= 1


        for k, v in f_map.items():
            if v != 0:
                return False            

        return True