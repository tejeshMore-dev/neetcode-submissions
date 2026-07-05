class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        sMap = {}

        for char in s1:
            s1Map[char] = s1Map.get(char, 0) +1
        
        lp = 0 
        rp = lp 

        while rp < len(s2):
            char = s2[rp]
            sMap[char] = sMap.get(char, 0) + 1

            while lp <= rp and sMap[char] > s1Map.get(char, 0):
                sMap[s2[lp]] -= 1
                
                if sMap[s2[lp]] == 0:
                    del sMap[s2[lp]]

                lp += 1
                
            
            if (rp - lp + 1) == len(s1):
                return True
            
            rp += 1
        
        return False