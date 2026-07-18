import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = []
        max_heap = []
        
        capital_zip = zip(capital, profits)

        for cp, pr in capital_zip:
            heapq.heappush(min_heap, (cp, pr))
        

        while k > 0:
            while min_heap and min_heap[0][0] <= w:
                cp, pr = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-pr, cp))
            
            if max_heap:
                pr, cp = heapq.heappop(max_heap)
                w += abs(pr)


            
            k -= 1


        return w