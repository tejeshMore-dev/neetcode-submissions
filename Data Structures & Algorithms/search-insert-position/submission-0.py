class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid = lp + (rp - lp) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lp = mid + 1
            else:
                rp = mid - 1
        
        return lp
        