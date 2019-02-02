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
        return isSame(p, q)
    
def isSame(p, q):
    if p is None or q is None:
        return True if p == q else False
    
    if p.val == q.val:
        l = isSame(p.left, q.left)
        r = isSame(p.right,q.right)
        return l and r
    else:
        return False
        
        
        
            