# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is None:
            return True
        if p and q is None:
            return False
        if p is None and q:
            return False
        if p.val == q.val:
            l = isSameTree(p.left, q.left)
            r = isSameTree(p.right,q.right)
            return l and r
            