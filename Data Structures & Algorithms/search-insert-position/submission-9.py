class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        
        lp = 0
        rp = len(nums)-1

        while lp <= rp:
            mid = lp + (rp-lp)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lp = mid + 1
            else:
                rp = mid - 1
        
        return lp
