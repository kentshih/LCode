# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def minD(r):
            
            ans = 99
            if not root:
                return 0
            left = minD(r.left)
            right= minD(r.right)
            return min(left,right) + 1
        return minD(root)