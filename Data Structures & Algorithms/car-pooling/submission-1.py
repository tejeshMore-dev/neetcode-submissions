import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []
        
        for trip in trips:
            heapq.heappush(min_heap, (trip[1], trip[2], trip[0]))
        


        while min_heap:
            ele = heapq.heappop(min_heap)
            start = ele[0]
            end_i = ele[1]
            cur_capacity = ele[2]

            while min_heap and min_heap[0][0] < end_i:
                ele = heapq.heappop(min_heap)
                end = ele[1]
                cur_capacity += ele[2]

                if cur_capacity>capacity:
                    return False
                
                heapq.heappush(min_heap, (end_i + 1, end, ele[2]))

        
        return True