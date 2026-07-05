class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ref_max = nums[0]
        max_count = 1

        for num in nums[1:]:
            if num == ref_max:
                max_count += 1
            else:
                max_count -= 1
                if max_count == 0:
                    ref_max = num
                    max_count = 1

        return ref_max
        