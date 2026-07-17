class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1

        if nums[R] >= nums[L]:
            return nums[L]

        while L<=R:
            mid = L + (R-L)//2

            if mid>0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[R] >= nums[L]:
                return nums[L]

            if nums[L] <= nums[mid]: 
                L = mid+1
            else:
                R = mid-1        