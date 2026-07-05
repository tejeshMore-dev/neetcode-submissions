from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x,y in points:
            dist = sqrt((x)**2 + (y)**2)
            heapq.heappush(min_heap, [dist,x,y])
        
        results = []
        while k>0:
            elements = heapq.heappop(min_heap)
            results.append([elements[1],elements[2]])
            k-=1
        
        return results