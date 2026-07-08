class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')

        cur_sum = 0
        l = 0
        r = 0

        while r < len(nums):
            cur_sum += nums[r]
            cur_sum = max(cur_sum, nums[r])
            ans = max(ans, cur_sum)
            r += 1
            
        return ans