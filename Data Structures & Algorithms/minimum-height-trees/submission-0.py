from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node, parent):
            temp = 0
            for nei in graph[node]:
                if parent == nei or nei in visited:
                    continue
                temp = max(temp, dfs(nei, node)+1)
            
            return temp
        
        ans = []
        for node in range(n):
            visited = set()
            ans.append(dfs(node,-1))

        min_ans = min(ans)
        res = []

        for i, num in enumerate(ans):
            if num == min_ans:
                res.append(i)
        
        return res