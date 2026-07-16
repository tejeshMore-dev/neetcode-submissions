import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        cost = [[float('inf')]*(k+2) for _ in range(n)]

        for u,v,w in flights:
            graph[u].append((v,w))
            
        cost[src][0] = 0
        min_heap = []
        heapq.heappush(min_heap,(0,0,src))

        while min_heap:
            ele = heapq.heappop(min_heap)

            c_cost = ele[0]
            cur_k = ele[1]
            node = ele[2]
            new_k = cur_k+1

            if node == dst:
                return c_cost

            if cur_k>k+1 or new_k>k+1:
                continue
            
            for nei in graph[node]:
                n_cost = c_cost + nei[1]

                if n_cost < cost[nei[0]][new_k]:
                    cost[nei[0]][new_k] = n_cost
                    heapq.heappush(min_heap, (n_cost,new_k,nei[0]))
        
        
        return -1
