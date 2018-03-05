# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = cur = ListNode(None)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val,node))
        while q.qsize() > 0 :
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val,cur.next))
        return ans.next