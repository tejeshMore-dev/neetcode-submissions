class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI = 0
        resL = 0

        def expand(l, r):
            nonlocal resL
            nonlocal resI
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resL:
                    resL = r - l + 1
                    resI = l
                l -= 1
                r += 1
            
        
        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i+1)
        
        return s[resI: resI + resL]