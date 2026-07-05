# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        def helper(node):
            nonlocal maxDiameter

            if not node:
                return 0
            
            leftH = helper(node.left)
            rightH = helper(node.right)

            maxDiameter  = max(maxDiameter, leftH + rightH)

            return 1 + max(leftH, rightH)
        
        helper(root)
        return maxDiameter
        