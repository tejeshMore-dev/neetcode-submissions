from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i,ele in enumerate(equations):
            u,v = ele
            graph[u].append((v,values[i]))
            graph[v].append((u,1/values[i]))

        visited = set()
        def dfs(cur, target, product):
            if cur == target:
                return product
            
            visited.add(cur)

            for nei in graph[cur]:
                if nei[0] in visited:
                    continue
                ele = nei[0]
                val = nei[1]
                ans = dfs(ele, target, product*val)
                if ans != -1:
                    return ans

            return -1

        ans = []
        for query in queries:
            u, v = query

            if u not in graph or v not in graph:
                ans.append(-1.0)
                continue
            
            visited = set()
            ans.append(dfs(u,v,1.0))

        return ans