class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        mem = {}

        def helper(i, cur_sum):
            if (i,cur_sum) in mem:
                return mem[(i,cur_sum)]

            if i==len(nums):
                if cur_sum == target:
                    return 1
                
                return 0
            
            ans = helper(i+1, cur_sum+nums[i]) + helper(i+1, cur_sum-nums[i])
            mem[(i,cur_sum)] = ans
            return ans
            
        return helper(0, 0)