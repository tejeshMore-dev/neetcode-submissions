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
            node = node.next 
            total += 1
        
        groups = 0
        cnt = 0

        node = head
        dummy = ListNode()
        before = dummy

        while groups < total // k:
            new_before = node
            prev = None

            while cnt < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp

                cnt += 1             
            
            before.next = prev
            new_before.next = node
            before = new_before
            cnt = 0
            groups += 1
        
        return dummy.next

         
        