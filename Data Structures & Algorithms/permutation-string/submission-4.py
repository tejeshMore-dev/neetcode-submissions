class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}

        for char in s1:
            if char not in s1_map:
                s1_map[char] = 0
            
            s1_map[char] += 1

        L = 0

        for R in range(len(s2)):
            if s2[R] not in s1_map:
                while L <= R:
                    if s2[L] in s1_map:
                        s1_map[s2[L]] += 1
                    L += 1
            else:
                s1_map[s2[R]] -= 1
                if s1_map[s2[R]] < 0:
                    while s1_map[s2[R]] < 0:
                        if s2[L] in s1_map:
                            s1_map[s2[L]] += 1
                        L += 1
                
                if R - L == len(s1) - 1:
                    return True
        
        return False
