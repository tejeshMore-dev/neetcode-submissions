class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s)-1

        dp = {}

        def is_palindrome(l,r):
            s1 = s[l:r+1]
            return s1 == s1[::-1]

        def helper(l,r):

            if (l,r) in dp:
                return dp[(l,r)]

            if l>r:
                return ""
            
            if s[l] == s[r]:
                if is_palindrome(l,r):
                    return s[l:r+1]

            s1 = helper(l+1,r)
            s2 = helper(l,r-1)

            if len(s1) >= len(s2):
                dp[(l+1,r)] = s1
                return s1
            else:
                dp[(l,r-1)] = s2
                return s2
        
        return helper(l,r)