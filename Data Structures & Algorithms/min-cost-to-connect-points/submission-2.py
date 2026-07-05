import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()

        min_heap = []
        heapq.heappush(min_heap, (0, points[0]))
        mst_cost = 0

        while min_heap:
            cost, point = heapq.heappop(min_heap)

            if len(visited) == len(points):
                return mst_cost

            if (point[0], point[1]) in visited:
                continue
            
            visited.add((point[0], point[1]))
            mst_cost += cost

            for new_point in points:
                if (new_point[0], new_point[1]) not in visited:
                    dist = abs(point[0]-new_point[0]) + abs(point[1]-new_point[1])
                    heapq.heappush(min_heap, (dist, new_point))
        
        return mst_cost





