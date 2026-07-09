import sys
sys.setrecursionlimit(20000)

class Solution:
    def numSquares(self, n: int) -> int:
        MAX = float('inf')
        mem = {}

        def helper(i, cur_sum):
            if (i, cur_sum) in mem:
                return mem[(i, cur_sum)]

            if cur_sum == n:
                return 0

            if cur_sum > n or i * i > n:
                return MAX

            ans = min(
                helper(i, cur_sum + i * i) + 1,
                helper(i + 1, cur_sum)
            )

            mem[(i, cur_sum)] = ans
            return ans

        return helper(1, 0)