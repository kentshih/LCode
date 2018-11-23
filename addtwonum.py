# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        self = ListNode(0)
        start = self
        while l1 != None and l2 != None:
            self.val = ( l1.val + l2.val + self.val )
            
            if self.val > 9:
                self.val = self.val % 10
                self.next = ListNode(1)
            elif l1.next != None or l2.next != None:
                self.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            self = self.next
            
        temp = None
        
        if l1 != None:
            temp = l1
        if l2 != None:
            temp = l2
        if temp != None:
            self.val += temp.val
            self.next = temp.next
        else:
            return start
            
        
        while self.val > 9:
            self.val = self.val % 10
            if self.next == None:
                self.next = ListNode(1)
            else:
                self.next.val += 1
            self = self.next
        
        return start
        