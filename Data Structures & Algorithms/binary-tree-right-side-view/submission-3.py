from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = deque([root])
        if not root:
            return []

        while queue:
            # ans = []
            res.append(queue[-1].val)
            length = len(queue)
            for _ in range(length):
                ele = queue.popleft()

                # if ele:
                #     ans.append(ele.val)
                
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
        
        return res
            
