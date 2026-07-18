# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def helper(node):
            nonlocal ans

            if not node:
                return 0
            
            l = max(helper(node.left),0)
            r = max(helper(node.right),0)

            p1 = l+node.val
            p2 = r+node.val

            gain = max(p1,p2)

            ans = max(ans, node.val+l+r)

            return gain
        
        helper(root)
        return ans
