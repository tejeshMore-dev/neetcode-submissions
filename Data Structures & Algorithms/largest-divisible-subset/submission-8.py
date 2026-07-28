import sys
sys.setrecursionlimit(200000)

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = []

        def helper(i, m, path):
            # print(path)
            nonlocal ans
            if len(path) > len(ans):
                ans = path.copy()

            if i == len(nums):
                return 
                
            if nums[i] % m == 0:
                path.append(nums[i])
                helper(i + 1, nums[i], path.copy())
                path.pop()
            
            helper(i+1, m, path)
            

        helper(0, 1, [])
        return ans
'''

1 % 2 
2 % 1









'''