# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i]=self.mergetwo(lists[i-1], lists[i])
        return lists[-1]    
        
    def mergetwo(self, l1, l2):
        head=ListNode(-1)   
        dummy=head
        while l1 and l2:
            if l1.val<l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1:
            dummy.next=l1
        else:
            dummy.next=l2
        return head.next 