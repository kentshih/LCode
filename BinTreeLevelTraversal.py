# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def GetHeight(root):
            if not root:
                return 0
            left  = GetHeight(root.left)
            right = GetHeight(root.right)
            return max(left,right) + 1
        
        ans = []
        def DFS(root, ans):
            if not root:
                return []
            else:
                return  