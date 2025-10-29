# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getlength(self, head):
        length=0
        current = head
        while current:
            length+=1
            current = current.next
        return length
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = self.getlength(list1)
        l2 = self.getlength(list2)

        a1,a2=[],[]
        current = list1
        for i in range(l1):
            if current:
                a1.append(current.val)
                current=current.next
        current = list2
        for i in range(l2):
            if current:
                a2.append(current.val)
                current=current.next

        a3 = a1+a2
        a3.sort()
        
        if not a3:
            return None
        
        head = ListNode(a3[0])
        current = head

        for value in a3[1:]:
            current.next = ListNode(value)
            current = current.next

        return head