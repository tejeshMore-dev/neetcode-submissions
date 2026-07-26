# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        c = 0

        while l1 or l2 or c:
            total  = 0
            
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next

            if c:
                total += c
            

            val = total % 10
            c = total // 10
            node.next = ListNode(val)
            node = node.next

            


        return dummy.next            