class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}

        def helper(i, last):
            if (i, last) in mem:
                return mem[(i, last)]

            if i == len(nums):
                return 0
            
            ans = helper(i+1, last)

            if nums[i] > last:
                ans = max(ans, helper(i+1, nums[i]) + 1)

            mem[(i, last)] = ans
            
            return ans


        return helper(0,-10001)