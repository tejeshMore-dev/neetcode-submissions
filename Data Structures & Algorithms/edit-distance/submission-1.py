class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        mem = {}

        def helper(i, j):
            if (i,j) in mem:
                return mem[(i,j)]

            if i>=len(word1) and j>=len(word2):
                return 0
            
            if i>=len(word1) and j<len(word2):
                return len(word2) - j
            if i<len(word1) and j>=len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                ans = helper(i+1, j+1)
            else:
                ans = min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))+1
            
            mem[(i,j)] = ans
            return ans

        return helper(0, 0)