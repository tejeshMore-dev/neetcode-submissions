from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            graph[a].append((b, v))
            graph[b].append((a, 1/v))
        
        def helper(a, b):
            queue = deque([(a, 1)])
            visited = set(a)
            
            while queue:
                node, ans = queue.popleft()

                if node == b:
                    return ans

                for nei, w in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, ans * w))

            return -1

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1)
            else:
                ans.append(helper(a,b))
            
        return ans
