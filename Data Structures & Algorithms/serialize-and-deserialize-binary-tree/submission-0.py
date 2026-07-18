# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        ans = ""
        queue = deque([])
        queue.append(root)

        while queue:

            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                
                if not node:
                    ans += "N#"
                    continue
                
                ans += f"{node.val}#"
                queue.append(node.left)
                queue.append(node.right)
        
        return ans
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        input = data.split('#')[:-1]
        
        queue = deque([])

        if input[0]=='N':
            return None

        root = TreeNode(int(input[0]))
        queue.append(root)
        i = 1

        while queue:
            node = queue.popleft()

            if input[i] != 'N':
                node.left = TreeNode(int(input[i]))
                queue.append(node.left)
            
            i+=1
            
            if input[i] != 'N':
                node.right = TreeNode(int(input[i]))
                queue.append(node.right)
            
            i+=1

        return root



            


            

            


