# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        
        def helper(node):
            nonlocal result

            if not node:
                return 0
            
            leftH = helper(node.left)
            rightH = helper(node.right)

            if abs(leftH - rightH) > 1:
                result = False
            
            return 1 + max(leftH, rightH)

        helper(root)
        return result