# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        end = prev
        cur = end
        prev = None
        while n>1:
            prev = cur
            cur = cur.next
            n -= 1
        
        if prev == None:
            temp = end
            end = end.next
            temp.next = None
        else:
            prev.next = cur.next
            cur.next = None
        
        prev = None
        cur = end
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

        

        
