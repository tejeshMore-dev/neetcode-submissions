class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        INF = float('inf')
        mem = {}

        def helper(p1, p2):
            if (p1, p2) in mem:
                return mem[(p1,p2)]

            if p1 >= len(text1) and p2 <= len(text2):
                return 0

            if p2 >= len(text2) and p1 <= len(text1):
                return 0
            
            ans = -INF
            if text1[p1] == text2[p2]:
                ans = max(ans,helper(p1+ 1, p2+1) + 1)
            else:
                ans = max(ans,helper(p1, p2+1))
                ans = max(ans,helper(p1+1, p2))

            mem[(p1,p2)] = ans
            return ans

        return helper(0,0)