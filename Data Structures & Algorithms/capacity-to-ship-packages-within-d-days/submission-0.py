from math import ceil

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lp = max(weights)
        rp = sum(weights)

        def days_required(min_weight):
            days = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight <= min_weight:
                    current_weight += weight
                else:
                    days += 1
                    current_weight = weight
            
            return days

        while lp <= rp:
            mid = lp + (rp - lp) // 2

            result  = days_required(mid)

            if result <= days:
                rp = mid - 1
            else:
                lp = mid + 1

        return lp
