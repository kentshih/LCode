# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new = self
        fix = self
        self.next = head
        while new.next:
            if n:
                n -= 1
            else:
                fix = fix.next
            new = new.next
        fix.next = fix.next.next
        return self.next