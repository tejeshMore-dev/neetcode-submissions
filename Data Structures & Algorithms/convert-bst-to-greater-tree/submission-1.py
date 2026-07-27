import sys
sys.setrecursionlimit(200000)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = 0

        def helper(node):
            nonlocal sum

            if not node:
                return
            
            helper(node.right)
            
            sum += node.val
            node.val = sum
            
            helper(node.left)
        
        helper(root)
        return root       
    
'''
     10
   9    15
  4    12  19
 2 5  11
  

'''