class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            res = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1]
                l -= 1
                r += 1
            
            return res
        
        ans = ""
        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i+1)

            if len(s1) > len(ans):
                ans = s1
            
            if len(s2) > len(ans):
                ans = s2
        
        return ans