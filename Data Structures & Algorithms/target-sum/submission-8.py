class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        mem = {}

        def helper(i, s):
            if (i, s) in mem:
                return mem[(i, s)]

            nonlocal ans
            
            if i == len(nums):
                if s == target:
                    return 1
                
                return 0

            ans1 = helper(i+1, s + nums[i])
            ans2 = helper(i+1, s - nums[i])

            ans = ans1 + ans2

            mem[(i, s)] = ans
            return ans
        
        helper(0, 0)
        return ans