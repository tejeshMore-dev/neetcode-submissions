class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f_map = {
            5: 0,
            10: 0,
            20: 0
        }
        
        for bill in bills:
            f_map[bill] += 1
            if bill == 5:
                continue
            elif bill == 10:
                if f_map[5]>0:
                    f_map[5] -= 1
                else:
                    return False
            elif bill == 20:
                if f_map[10]>0 and f_map[5]>0:
                    f_map[10] -= 1
                    f_map[5] -= 1
                elif f_map[5]>=3:
                    f_map[5] = f_map[5]-3
                else:
                    return False
        return True 