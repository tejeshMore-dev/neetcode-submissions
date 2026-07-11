from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        ans = 0
        prefix = 0

        for i, num in enumerate(nums):
            ans += prefix_map[ prefix + num - k]
            prefix = prefix + num 
            prefix_map[prefix] += 1 
        
        return ans