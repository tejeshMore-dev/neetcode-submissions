class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def helper(i, cur_sum):            
            if i==len(nums):
                if cur_sum == target:
                    return 1
                
                return 0
            
            return helper(i+1, cur_sum+nums[i]) + helper(i+1, cur_sum-nums[i])
            
        return helper(0, 0)