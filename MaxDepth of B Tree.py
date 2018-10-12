# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxD(cur):
            if not cur:
                return 0
            ans = 1
            if not cur.left and not cur.right:
                return ans
            left = maxD(cur.left)
            right= maxD(cur.right)
            return max(left,right) + ans
        return maxD(root)
        