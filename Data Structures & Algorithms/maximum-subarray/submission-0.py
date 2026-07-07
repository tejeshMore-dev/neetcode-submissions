class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')

        cur_sum = 0
        l = 0
        r = 0

        while r < len(nums):
            cur_sum += nums[r]
            ans = max(ans, cur_sum)
            while l<=r and cur_sum < 0:
                cur_sum -= nums[l]
                l += 1
            r += 1
            
        return ans