from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = defaultdict(list)

        i = 0
        n = len(s)

        while i < n:
            r = 0
            while  i < n and r < numRows:
                row[r].append(s[i])
                r += 1
                i += 1

            r = numRows - 2
            while i < n and r > 0:
                row[r].append(s[i])
                r -= 1
                i += 1

        ans = []
        for k, v in row.items():
            ans += v

        return "".join(ans)
        