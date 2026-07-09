class Solution:
    def numDecodings(self, s: str) -> int:
        mem  = {}
        
        def helper(i):
            if i in mem:
                return mem[i]

            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            ans = helper(i+1)
            
            if i + 1 < len(s) and int(s[i:i +2]) < 27:
                ans += helper(i+2)

            mem[i] = ans

            return ans

        return helper(0)
