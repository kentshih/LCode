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
            if not r:
                return 0
            if not r.left and not r.right:
                return 1
            left = minD(r.left) 
            right= minD(r.right) 
            if left != 0 and right != 0:
                return min(left,right) + 1
            elif left == 0:
                return right + 1
            else:
                return left + 1
        return minD(root)