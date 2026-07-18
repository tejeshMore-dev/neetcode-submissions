from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = defaultdict(set)
        graph = defaultdict(list)

        indegree = [0]*numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([])

        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)

        while queue:
            ele = queue.popleft()

            for nei in graph[ele]:
                pre[nei] |= pre[ele]
                pre[nei].add(ele)

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        ans = []
        for u,v in queries:
            if u in pre[v]:
                ans.append(True)
            else:
                ans.append(False)

        return ans


