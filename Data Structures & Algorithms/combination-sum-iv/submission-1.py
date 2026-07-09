class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        mem = {}
        def dfs(cur_sum):
            if cur_sum in mem:
                return mem[cur_sum]

            if cur_sum == target:
                return 1
            
            if cur_sum>target:
                return 0

            ans = 0
            for j in range(len(nums)):
                ans += dfs(cur_sum + nums[j])
            mem[cur_sum] = ans
                

            return ans
        
        return dfs(0)