# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        node = dummyNode
        carry = 0

        while l1 or l2 or carry:
            currentSum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = currentSum // 10
            currentSum = currentSum % 10
            
            newNode = ListNode(currentSum)
            node.next = newNode
            node = newNode

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            
            if l1 and not l2 and not carry:
                node.next = l1
            
            if l2 and not l1 and not carry:
                node.next = l2
        
        return dummyNode.next

            
