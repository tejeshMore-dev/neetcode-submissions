# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(n1,n2):
            if n1 and not n2:
                return False
            
            if n2 and not n1:
                return False
            
            if not n1 and not n2:
                return True
            
            if n1.val != n2.val:
                return False
            
            return check(n1.left,n2.left) and check(n1.right,n2.right)

        def iterate(n1):
            if not n1:
                return False
            
            result = False
            if n1.val == subRoot.val:
                result = check(n1,subRoot)

            if result:
                return True
            
            return iterate(n1.left) or iterate(n1.right)
        
        return iterate(root)

            
            
