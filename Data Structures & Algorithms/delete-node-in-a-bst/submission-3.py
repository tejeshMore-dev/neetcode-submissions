# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def remove(root, k):
            if not root:
                return None
            
            if root.val == k:
                if not root.left and not root.right:
                    return None
                elif root.left and not root.right:
                    return root.left
                elif root.right and not root.left:
                    return root.right
                else:
                    # Find inorder successor
                    succ = root.right
                    while succ.left:
                        succ = succ.left

                    root.val = succ.val
                    root.right = remove(root.right, succ.val)
                    return root
            if root.val < k:
                root.right = remove(root.right, k)
            else:
                root.left = remove(root.left, k)
            return root

        return remove(root, key)