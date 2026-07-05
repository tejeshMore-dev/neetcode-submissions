class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if not count:
                count += 1
                candidate = num
            elif num is candidate:
                count += 1
            else:
                count -= 1

        return candidate