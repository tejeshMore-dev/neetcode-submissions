class Solution:
    def mySqrt(self, x: int) -> int:
        lp = 0
        rp = x
        
        while lp <= rp:
            mid =  lp + (rp - lp) // 2
            
            if mid *  mid == x:
                return mid
            elif mid * mid > x:
                rp = mid - 1
            else:
                lp = mid + 1
        
        return rp