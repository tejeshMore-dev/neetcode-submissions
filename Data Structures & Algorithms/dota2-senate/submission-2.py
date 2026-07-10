from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = deque([])
        d_q = deque([])
        last = 0 
        for i, sen in enumerate(senate):
            if sen == "R":
                r_q.append(i)
            else:
                d_q.append(i)
            
            last = i
        
        while r_q and d_q:            
            r =  r_q.popleft()
            d = d_q.popleft()

            if r < d:
                r_q.append(last + 1)
            else:
                d_q.append(last + 1)
            
            last += 1

        if r_q:
            return "Radiant"

        return "Dire"