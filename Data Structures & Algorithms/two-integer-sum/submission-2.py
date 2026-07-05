class Solution:
    def __init__(self):
        self._seen = {}

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            diff = target - num

            if diff in self._seen:
                return [self._seen[diff], i]

            self._seen[num] = i
        