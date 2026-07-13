class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        mem = {}

        def dfs(i):
            if i in mem:
                return mem[i]

            if i == len(s):
                return 0

            ans = 1 + dfs(i+1)

            for j in range(i, len(s)):
                if s[i:j+1] in dict_set:
                    ans = min(ans, dfs(j+1))
            
            mem[i] = ans
            return ans

        return dfs(0)        