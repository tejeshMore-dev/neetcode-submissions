# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sp = dummy
        fp = dummy
        
        while n >= 0:
            fp = fp.next
            n -= 1
        
        while fp:
            fp = fp.next
            sp = sp.next
        
        sp.next = sp.next.next
    
        return dummy.next
        
        