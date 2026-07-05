class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f_map = {}
        max_f = 0
        L = 0
        ans = 0

        for R in range(len(s)):
            if s[R] not in f_map:
                f_map[s[R]] = 0
            
            f_map[s[R]] += 1

            max_f = max(f_map[s[R]], max_f)

            while R - L + 1 - max_f > k:
                f_map[s[L]] -= 1
                L += 1
            
            ans = max(ans, R-L+1)

        return ans                



        