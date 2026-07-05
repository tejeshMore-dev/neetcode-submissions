class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p0 = 0 
        p1 = 0

        ans = ""

        while p0<len(word1) or p1<len(word2):
            if p0>=len(word1) and p1<len(word2):
                ans += word2[p1:]
                break
            elif p1>=len(word2) and p0<len(word1):
                ans += word1[p0:]
                break
            else:
                ans += word1[p0]
                ans += word2[p1]
                p0 += 1
                p1 += 1
        
        return ans
            