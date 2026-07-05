class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for v in range(0,n):
            graph[v] = []

        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1) 

        visited = set()
        component_cnt = 0

        def dfs(node):
            visited.add(node)

            for edge_node in graph[node]:
                if edge_node not in visited:
                    dfs(edge_node)

        
        for v,e in graph.items():
            if v not in visited:
                dfs(v)
                component_cnt += 1
        
        return component_cnt