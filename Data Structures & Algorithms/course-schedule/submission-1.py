class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[v].append(u)
        
        visited = set()
        path = set()

        def hasCycle(i):
            visited.add(i)
            path.add(i)
            for nei in graph[i]:
                if nei in visited and nei in path:
                    return True
                if hasCycle(nei):
                    return True
            path.remove(i)
            return False


        for i in range(numCourses):
            if i not in visited:
                if hasCycle(i):
                    return False
        
        return True
        