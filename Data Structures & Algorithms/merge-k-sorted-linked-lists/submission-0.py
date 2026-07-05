# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(head1, head2):
            ans = ListNode()
            tmp = ans

            while head1 and head2:
                if head1.val <= head2.val:
                    tmp.next = head1
                    head1 = head1.next
                else:
                    tmp.next = head2
                    head2 = head2.next
                tmp = tmp.next
            
            if not head2:
                tmp.next = head1
             
            if not head1:
                tmp.next = head2

            return ans.next

        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            return merge(lists[0],lists[1])
        
        a = lists[0]
        b = lists[1]

        a = merge(a,b)

        for item in lists[2:]:
            a = merge(a, item)
        
        return a
