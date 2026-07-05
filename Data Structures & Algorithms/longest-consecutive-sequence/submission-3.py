class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set(nums)
        res = 1

        for num in nums:
            count = 0
            if num - 1 not in seen:
                while num  in seen:
                    num += 1
                    count += 1
                    res = max(res, count)

        return res
        