class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(i):
            if i in mem:
                return mem[i]

            if i >= len(nums):
                return 0
               
            ans = max(dfs(i+2) + nums[i], dfs(i+1))
            mem[i] = ans
            return ans

        if len(nums)<2:
            return nums[0]
        return max(dfs(0),dfs(1))
    
