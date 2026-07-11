class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        ans = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                to_find = target - nums[j] - nums[i]
                l = j+1
                r = len(nums)-1
                while l<r:
                    if to_find == nums[l]+nums[r]:
                        ans.add(tuple([nums[i],nums[j],nums[l],nums[r]]))
                        l+=1
                        r-=1
                    elif nums[l] + nums[r] > to_find:
                        r -= 1
                    else:
                        l += 1
                
        return list(ans)