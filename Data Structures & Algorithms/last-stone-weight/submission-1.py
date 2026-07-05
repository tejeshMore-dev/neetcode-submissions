
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1*stone)

        while len(max_heap)>1:
            x = -1*heapq.heappop(max_heap)
            y = -1*heapq.heappop(max_heap)

            temp = abs(x-y)
            if temp!=0:
                heapq.heappush(max_heap, -1*temp)
            
        if len(max_heap):
            return -max_heap[0]
        return 0
