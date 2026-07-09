class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2

        if sum(nums) % 2:
            return False

        def helper(i, cur_sum):
            if cur_sum>target:
                return False
            
            if cur_sum == target:
                return True
            
            if i>=len(nums):
                return False

            return helper(i+1, cur_sum+nums[i]) or helper(i+1, cur_sum)
            
        return helper(0, 0)