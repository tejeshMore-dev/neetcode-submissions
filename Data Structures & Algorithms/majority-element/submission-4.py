class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if not count:
                candidate = num
            
            if num is candidate:
                count += 1
            else:
                count -= 1

        return candidate