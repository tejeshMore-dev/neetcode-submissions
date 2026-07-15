from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        cnt = 0

        while queue:
            ele = queue.popleft()
            cnt+=1
            res.append(ele)

            for nei in graph[ele]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        if cnt == numCourses:
            return res
        return []


