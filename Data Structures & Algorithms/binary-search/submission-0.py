class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1


        while lp <= rp:
            mid = lp + (rp - lp) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lp = mid + 1
            else:
                rp = mid -1
        
        return -1