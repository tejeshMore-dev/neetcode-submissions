class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = n + 1 
            
        for i in range(len(nums)):
            val = abs(nums[i])

            if 1 <= val <= n:
                nums[val - 1] = -abs(nums[val - 1])

            
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
            
        return n + 1

            
        


    

        