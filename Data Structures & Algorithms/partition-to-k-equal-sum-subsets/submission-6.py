class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        path = set()
        total = sum(nums)
        sorted(nums)
        nums.sort(reverse=True)
        
        if total % k != 0:
            return False
        target = total // k

        def dfs(start, cur_sum, sets):
            nonlocal target
            if sets == k :
                return True

            if cur_sum == target:
                return dfs(0, 0, sets + 1)


            for i in range(start, len(nums)):
                if i in path:
                    continue

                if cur_sum + nums[i] > target:
                    continue

                path.add(i)
                if dfs(i+1, cur_sum + nums[i], sets):
                    return True
                path.remove(i)
                
            return False

        return dfs(0, 0, 0)


        