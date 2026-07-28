class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        INF = float('inf')
        n = len(nums)

        for i in range(n):
            l = r = -INF
            if i - 1 >= 0 :
                l = nums[i-1]
            
            if i + 1 < n:
                r = nums[i+1] 
            
            # print(l, nums[i], r)
            if l <= nums[i] and nums[i] >= r:
                return i


        