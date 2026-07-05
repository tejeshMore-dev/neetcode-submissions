import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        INF = float('inf')
        dist = [INF] * n
    
        graph = {}

        for u,v,w  in times:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v,w))
                

        min_heap = []
        heapq.heappush(min_heap,(0,k))

        while min_heap:

            ele = heapq.heappop(min_heap)
            cost = ele[0]
            node = ele[1]
            if cost >= dist[node-1]:
                continue

            dist[node-1] = cost
            
            for e in graph[node]:
                up_cost = e[1] + cost
                # if up_cost < dist[e[0]-1]:
                #     dist[e[0]-1] = up_cost
                
                heapq.heappush(min_heap,(up_cost, e[0]))
            
            
        
        ans = max(dist)
        if ans == INF:
            return -1
        return ans



