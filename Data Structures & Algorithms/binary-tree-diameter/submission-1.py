# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def helper(node):
            nonlocal diameter
            
            if not node:
                return 0
            
            l_depth = helper(node.left)
            r_depth = helper(node.right)

            diameter = max(diameter, l_depth + r_depth)

            return 1 + max(l_depth, r_depth)

        helper(root)
        return diameter

        