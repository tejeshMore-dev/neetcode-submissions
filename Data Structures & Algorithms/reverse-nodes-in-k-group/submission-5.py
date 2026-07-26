# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total = 0 
        node = head

        while node:
            total += 1
            node = node.next

        total_groups = total // k

        dummy = ListNode()
        dummy.next = head 
        node = dummy

        start = node
        new_end = node.next

        group = 0
        node = node.next
        
        while group < total_groups:
            cnt = 0
            prev = None
            
            while cnt < k and node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                cnt += 1
        
            start.next = prev
            new_end.next = node
            start = new_end
            new_end = node
            
            group += 1
        

        return dummy.next




        