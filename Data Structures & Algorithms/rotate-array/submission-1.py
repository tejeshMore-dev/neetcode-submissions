class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        e = len(nums) - 1
        k = k%len(nums)

        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        
        s = 0
        e = k-1

        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        
        s = k
        e = len(nums)-1

        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
