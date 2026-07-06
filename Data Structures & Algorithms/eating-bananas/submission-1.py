from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1
        rp = max(piles)

        def hour_required(rate):
            ans = 0 
            for pile in piles:
                ans += ceil(pile/rate)

            return ans

        while lp <= rp:
            mid = lp + (rp - lp) // 2

            result = hour_required(mid)

            if result <= h:
                rp = mid - 1
            else:
                lp = mid + 1
        
        return lp
        