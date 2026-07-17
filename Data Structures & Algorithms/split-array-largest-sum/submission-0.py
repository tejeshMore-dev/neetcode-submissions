class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = max(nums)
        r = sum(nums)

        ans = l

        def calc(limit):
            cnt = 1
            cur_sum = 0

            for num in nums:
                if cur_sum + num <= limit:
                    cur_sum += num
                else:
                    cnt += 1
                    cur_sum = num
            
            return cnt <= k


        while l <= r:
            mid = l + (r - l) // 2

            if calc(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

