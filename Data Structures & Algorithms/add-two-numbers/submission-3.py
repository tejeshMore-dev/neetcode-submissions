# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        cur = ans

        def calculate(val1, val2):
            nonlocal carry

            sum = val1 + val2 + carry
            val = sum % 10
            carry = sum // 10
            return val

        while l1 or l2:
            if l1 and not l2:
                val = calculate(l1.val,0)
                cur.next = ListNode(val)
                cur = cur.next
                l1 = l1.next
            elif l2 and not l1:
                val = calculate(0,l2.val)
                cur.next = ListNode(val)
                cur = cur.next
                l2 = l2.next
            else:
                val = calculate(l1.val,l2.val)
                cur.next = ListNode(val)
                cur = cur.next
                l1 = l1.next
                l2 = l2.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return ans.next

