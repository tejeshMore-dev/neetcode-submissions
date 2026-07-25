# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_list(l1, l2):
            head = ListNode()
            node = head
            while l1 or l2:
                if not l2:
                    node.next = l1
                    break

                if not l1:
                    node.next = l2
                    break
                
                if l1.val <= l2.val:
                    node.next = l1
                    node = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    node = l2
                    l2 = l2.next

            return head.next
        
        list1= lists[0]

        for i in range(1, len(lists)):
            list1 = merge_list(list1, lists[i])
        
        return list1
