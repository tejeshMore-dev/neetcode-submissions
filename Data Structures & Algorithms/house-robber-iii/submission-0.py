# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:
        mem = {}

        def helper(node):
            if node in mem:
                return mem[node]

            if not node:
                return 0
            
            skip = helper(node.left) + helper(node.right)

            rob = node.val

            if node.left:
                rob += helper(node.left.left)
                rob += helper(node.left.right)
            
            if node.right:
                rob += helper(node.right.left)
                rob += helper(node.right.right)
            
            ans = max(skip, rob)
            mem[node] = ans

            return ans


        return helper(root)