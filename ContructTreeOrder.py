# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        io = len(inorder)
        po = len(postorder)
        if not po:
            return Null

        while inorder:
            rnum = postorder[-1]
            for i in range(inorder):
                if postorder[i] == rnum:
                    left = postorder[:i]
                    right= postorder[i:]
                    