class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid = lp + (rp - lp) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lp]:
                if nums[lp] <= target < nums[mid]:
                    rp = mid - 1
                else:
                    lp = mid + 1
            else:
                if nums[mid] < target <= nums[rp]:
                    lp = mid + 1
                else:
                    rp =mid - 1
        return -1