import sys
sys.setrecursionlimit(20000)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}

        def helper(i):
            if i in mem:
                return mem[i]

            if i >= len(nums) - 1:
                return True
            
            for jump in range(1, nums[i] + 1):
                if helper(i + jump):
                    mem[i] = True
                    return True

            mem[i] = False
            return False

        return helper(0)