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
        if not inorder or not postorder:
            return 0

        else:
        io = len(inorder)
        po = len(postorder)
        if po:
            root = TreeNode(postorder[-1])
        
        while inorder:
            left =buildT()
            right = buildT()