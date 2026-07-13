from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        f_map = Counter(s)
        max_heap = []

        for char, f in f_map.items():
            heapq.heappush(max_heap, (-f, char))
        

        ans  = []

        while max_heap:
            f, char = heapq.heappop(max_heap)
            if ans and char == ans[-1]:
                if not max_heap:
                    ans = []
                    break
                f1, char1 = heapq.heappop(max_heap)
                ans.append(char1)
                f1 = 1 + f1
                if f1 < 0:
                    heapq.heappush(max_heap, (f1, char1))
            else:
                f = 1 + f
                ans.append(char)
            
            if f < 0:
                heapq.heappush(max_heap, (f, char))    
        
        return "".join(ans)
        

                    



