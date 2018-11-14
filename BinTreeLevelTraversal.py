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
        
        def DFS(root, ans, height):
            if not root:
                return ans
            else:
                ans[height].append(root.val)
                DFS(root.left, ans, height+1)
                DFS(root.right, ans, height+1)
                return ans 
        
        ans = []
        height = GetHeight(root)
        for x in xrange(height):
            ans.append([])
        if height == 0:
            return ans
        else:
            ans = DFS(root, ans, 0)
            return ans