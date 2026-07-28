class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mem = {}

        def helper(l, r):
            if (l, r) in mem:
                return mem[(l, r)]
                
            if l > r:
                return 0
            
            if l == r:
                return 1
            
            if s[l] == s[r]:
                mem[(l, r)] = 2 + helper(l + 1, r - 1)
            else:
                mem[(l, r)] = max(helper(l + 1, r), helper(l, r - 1))

            return mem[(l, r)]
        
        return helper(0, len(s) - 1)


        