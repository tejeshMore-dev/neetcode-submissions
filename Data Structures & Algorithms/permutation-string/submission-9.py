from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        
        for char in s1:
            s1_map[char] += 1

        n1 = len(s1)
        l = 0

        for r in range(len(s2)):            
            if s2[r] not in s1_map:
                while l <= r:
                    s2_map[s2[l]] -= 1
                    l += 1
                     
                    
            else:
                s2_map[s2[r]] += 1

                if s2_map[s2[r]] > s1_map[s2[r]]:
                    while s2_map[s2[r]] > s1_map[s2[r]]:
                        s2_map[s2[l]] -= 1
                        l += 1
                        
                    
                if r - l + 1 == n1:
                    return True 

        return False
        