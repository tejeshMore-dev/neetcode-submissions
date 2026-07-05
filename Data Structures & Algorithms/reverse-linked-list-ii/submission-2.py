# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        prev = None
        diff = right-left+1

        while left > 1:
            prev = node
            node = node.next
            left -= 1
        
        left_node = node
        left_prev = prev
        

        prev = None

        while diff > 0 and node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            diff -= 1
        
        if node:
            left_node.next = node
        
        
        if left_prev:
            left_prev.next = prev
        else:
            head = prev

        return head
        

        


        