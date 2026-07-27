from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        mem = {}

        for u, v in prerequisites:
            graph[u].append(v)
        
        ans = []

        def reachable(u, v):
            if (u, v) in mem:
                return mem[(u, v)]

            queue = deque([u])
            visited = set()

            while queue:
                node = queue.popleft()
                visited.add(node)

                if node == v:
                    return True

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                        mem[(u, nei)] = True
                
                    
            return False

        for u, v in queries:
            ans.append(reachable(u, v))

        return ans
                