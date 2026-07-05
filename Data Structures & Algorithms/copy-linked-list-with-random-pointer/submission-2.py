"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_map = {}
        random_map = {}

        node = head

        while node:
            copy_node = Node(node.val)
            node_map[node] = copy_node
            node = node.next
        
        node = head

        while node:
            copy_node = node_map[node]
            if node.next:
                copy_node.next = node_map[node.next]
            else:
                copy_node.next = None
            if node.random:
                copy_node.random = node_map[node.random]
            else:
                copy_node.random = None
            node = node.next

        
        return node_map[head]