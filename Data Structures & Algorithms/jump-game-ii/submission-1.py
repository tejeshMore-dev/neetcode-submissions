class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [0] * len(nums)

        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]

            if i==len(nums)-1:
                return 0

            if i>=len(nums):
                return 0
            
            ans = float('inf')
            for j in range(nums[i]):
                ans = min(ans, helper(i+j+1)+1)
            
            mem[i] = ans
            return ans
        
        return helper(0)