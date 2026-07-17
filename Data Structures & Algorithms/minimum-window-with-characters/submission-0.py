from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_len = len(s)
        ans = ""

        t_counter = Counter(t)
        s_counter = defaultdict(int)
        l = 0
        r = 0
        have = 0
        req = len(t_counter)

        for r in range(len(s)):
            if s[r] in t_counter:
                s_counter[s[r]] += 1

                if s_counter[s[r]] == t_counter[s[r]]:
                    have += 1
            
            while have == req:
                if r - l + 1 <= ans_len:
                    ans_len = r - l + 1
                    ans = s[l:r+1]
                
                if s[l] in t_counter:
                    if s_counter[s[l]] == t_counter[s[l]]:
                        have -= 1
                    s_counter[s[l]] -= 1
                
                l += 1


        return ans
        


        
