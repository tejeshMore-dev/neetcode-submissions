class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
            
        graph = {}
        visited = set()

        for v, e in edges:
            if v not in graph:
                graph[v] = []
            if e not in graph:
                graph[e] = []
            
            graph[v].append(e)
            graph[e].append(v)

        def has_cycle(v, parent):
            if v in visited:
                return True
            
            visited.add(v)

            for edge_n in graph[v]:
                if edge_n == parent:
                    continue
                
                if has_cycle(edge_n, v):
                    return True
            
            return False

        if has_cycle(0, -1):
            return False

        return len(visited) == n