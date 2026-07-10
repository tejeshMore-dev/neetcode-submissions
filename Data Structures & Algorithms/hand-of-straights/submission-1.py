class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        f_map = {}

        for num in hand:
            if num not in f_map:
                f_map[num] = 0
            
            f_map[num] += 1
        

        for i, num in enumerate(sorted(hand)):
            if num not in f_map:
                continue
            
            max_ele = num + groupSize - 1
            cur = num
            while cur<=max_ele:
                if cur not in f_map:
                    return False

                
                f_map[cur] -= 1
                if f_map[cur] == 0:
                    del f_map[cur]
                cur+=1

        return True


