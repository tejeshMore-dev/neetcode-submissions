class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}

        def helper(i, last):
            if (i, last) in mem:
                return mem[(i, last)]

            if i == len(nums):
                return 0
            
            if nums[i] > last:
                a = helper(i+1, nums[i]) + 1
                b = helper(i+1, last)
                ans = max(a,b)
                mem[(i,last)] = ans
                return ans
            else:
                ans = helper(i+1, last)
                mem[(i, last)] = ans
                return ans


        return helper(0,-10001)