class Solution:
    def checkValidString(self, s: str) -> bool:
        mem = {}

        def helper(i, o, c):
            if (i, o, c) in mem:
                return mem[(i, o, c)]

            if i >= len(s):
                if o == c:
                    return True
                
                return False

            ans = False
            if s[i] == "*":
                ans = ans or helper(i+1, o+1, c)
                ans = ans or helper(i+1, o, c)
                if o >= c + 1:
                    ans = ans or helper(i+1, o, c+1)
            elif s[i] == "(":
                ans = ans or helper(i+1, o+1, c)
            else:
                if o < c + 1:
                    return False
                ans = ans or helper(i+1, o, c+1)

            mem[(i, o, c)] = ans
            return ans

        return helper(0, 0, 0)

