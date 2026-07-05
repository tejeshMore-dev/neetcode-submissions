class DSU:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}
        groups = {}
        ans = []

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name
                dsu.union(first_email, email)

        for email in email_to_name.keys():
            root = dsu.find(email)

            if root not in groups:
                groups[root] = []

            groups[root].append(email)
        
        for root_email, emails in groups.items():
            ans.append([email_to_name[root_email]] + sorted(emails))
    
        return ans

        