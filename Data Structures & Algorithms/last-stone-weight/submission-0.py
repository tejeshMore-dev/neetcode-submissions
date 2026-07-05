import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones ]
        heapq.heapify(stones)

        while len(stones) >=2:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))

            diff = x - y

            heapq.heappush(stones, diff * -1)
        
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
    