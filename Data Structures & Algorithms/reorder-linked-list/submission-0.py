# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow
        cur = mid.next
        mid.next = None
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        end = prev
        start = head


        while start and end:
            temp1 = start.next
            start.next = end
            start = temp1
            temp2 = end.next 
            end.next = temp1
            end = temp2
                        




