import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        e_heap = []
        p_heap = []
        n = 0

        for i, task in enumerate(tasks):
            n += 1
            heapq.heappush(e_heap, (task[0],task[1],i))
        
        ans = []
        time = 0
        
        while e_heap or p_heap:

            if not p_heap:
                time = max(time, e_heap[0][0])
            
            while e_heap and e_heap[0][0] <= time:
                e, p, i = heapq.heappop(e_heap)
                heapq.heappush(p_heap, (p,i))
            
            process, index = heapq.heappop(p_heap)
            ans.append(index)
            time += process
        
        return ans 




                

        return ans