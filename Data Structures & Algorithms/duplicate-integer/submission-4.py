class Solution:
    def __init__(self):
        self.seen = set()

    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in self.seen:
                return True
            self.seen.add(num)
        
        return False