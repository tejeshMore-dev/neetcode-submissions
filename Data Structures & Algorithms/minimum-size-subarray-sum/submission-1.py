class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 10001 
        c_sum = 0
        L = 0

        for R in range(len(nums)):
            c_sum = nums[R] + c_sum            

            while c_sum >= target:
                if c_sum >= target:
                    ans = min(ans, R - L + 1)

                c_sum -= nums[L]
                L += 1 

        if ans == 10001:
            return 0

        return ans