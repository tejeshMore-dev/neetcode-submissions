class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = {}

        for v1, v2 in trust:
            if v1 not in graph:
                graph[v1] = [0,0]
            if v2 not in graph:
                graph[v2] = [0,0]
            
            #[outward, inward]
            graph[v1][0] += 1
            graph[v2][1] += 1
        
        for v, e in graph.items():
            if e[0] == 0 and e[1] == n-1:
                return v

        return -1