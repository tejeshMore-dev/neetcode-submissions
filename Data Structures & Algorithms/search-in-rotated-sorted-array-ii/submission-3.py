class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = L + (R-L)//2

            if nums[mid] == target:
                return True

            # Cannot determine the sorted half
            if nums[L] == nums[mid] == nums[R]:
                L += 1
                R -= 1
            elif nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1

            
        return False