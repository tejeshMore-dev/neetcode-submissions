# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = dummy
        cnt = 0

        while cnt < left and node:
            prev = node
            node = node.next
            cnt += 1
        
        start = prev
        new_end = node

        cnt = 0 
        prev = None
        while cnt < right - left + 1 and node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            cnt += 1
        
        start.next = prev
        new_end.next = node
        
        return dummy.next
        

