class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        mem = {}

        def helper(i, cur_sum):
            if (i, cur_sum) in mem:
                return mem[(i, cur_sum)]

            if i == len(stones):
                return abs((total - cur_sum) - cur_sum)

            mem[(i, cur_sum)] = min(
                helper(i + 1, cur_sum),
                helper(i + 1, cur_sum + stones[i])
            )

            return mem[(i, cur_sum)]

        return helper(0, 0)