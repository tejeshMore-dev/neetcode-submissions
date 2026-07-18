class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent_a = list(range(n + 1))
        rank = [1] * (n+1)

        def parent(x):
            if parent_a[x] != x:
                parent_a[x] = parent(parent_a[x])

            return parent_a[x]


        def union(x, y):
            px = parent(x)
            py = parent(y)

            if px == py:
                return False

            if rank[px] > rank[py]:
                parent_a[py] = px
            elif rank[py] > rank[px]:
                parent_a[px] = py
            else:
                parent_a[py] = px
                rank[px] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]    
