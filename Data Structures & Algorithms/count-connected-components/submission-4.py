class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for v in range(0,n):
            graph[v] = []

        for v1, v2 in edges:
            if v1 not in graph:
                graph[v1] = []
            
            if v2 not in graph:
                graph[v2] = []
            
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for edge_n in graph[node]:
                if edge_n not in visited:
                    dfs(edge_n)

        result = 0
        for v,e in graph.items():
            if v not in visited:
                dfs(v)
                result += 1
        
        return result

        