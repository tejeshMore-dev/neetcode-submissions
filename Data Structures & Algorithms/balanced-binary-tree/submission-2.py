# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True, 0
            
            l_result, l_depth = helper(node.left)
            r_result, r_depth = helper(node.right)

            if not l_result or not r_result:
                return False, 0

            if abs(l_depth - r_depth) > 1:
                return False, 0
            
            return True, 1 + max(l_depth, r_depth)

        result, depth = helper(root)
        return result
        