# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, n1: Optional[ListNode], n2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head

        while n1 or n2:
            if n1 and not n2:
                head.next = n1
                break
            
            elif n2 and not n1:
                head.next = n2
                break
                
            else:
                if n1.val <= n2.val:
                    head.next = n1
                    head = n1
                    n1 = n1.next
                else:
                    head.next = n2
                    head = n2
                    n2 = n2.next
        
        return dummy.next