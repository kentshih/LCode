# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from operator import xor

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def start(root):
            if root is None:
                return True
            else:
                isSame(root.left, root.right)
            
        def isSame(left,right):
            if not left and not right:
                return True
            elif left != right:
            # elif xor(left,right):
                return False

            elif left.val == right.val:
                doout = isSame(left.left, right.right)
                doin  = isSame(left.right, right.left)
                return doleft and doright
            else:
                return False

        if not root:
            return False
        else:
            return isSame(root.left, root.right)
            