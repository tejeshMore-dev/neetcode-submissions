class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = sum(nums)

        curMax = maxSum = nums[0]
        for num in nums[1:]:
            curMax = max(num, curMax+num)
            maxSum = max(maxSum, curMax)
        
        if maxSum < 0:
            return maxSum
        
        curMin = minSum = nums[0]
        for num in nums[1:]:
            curMin = min(num, curMin+num)
            minSum = min(minSum, curMin)
        
        return max(maxSum, total-minSum)