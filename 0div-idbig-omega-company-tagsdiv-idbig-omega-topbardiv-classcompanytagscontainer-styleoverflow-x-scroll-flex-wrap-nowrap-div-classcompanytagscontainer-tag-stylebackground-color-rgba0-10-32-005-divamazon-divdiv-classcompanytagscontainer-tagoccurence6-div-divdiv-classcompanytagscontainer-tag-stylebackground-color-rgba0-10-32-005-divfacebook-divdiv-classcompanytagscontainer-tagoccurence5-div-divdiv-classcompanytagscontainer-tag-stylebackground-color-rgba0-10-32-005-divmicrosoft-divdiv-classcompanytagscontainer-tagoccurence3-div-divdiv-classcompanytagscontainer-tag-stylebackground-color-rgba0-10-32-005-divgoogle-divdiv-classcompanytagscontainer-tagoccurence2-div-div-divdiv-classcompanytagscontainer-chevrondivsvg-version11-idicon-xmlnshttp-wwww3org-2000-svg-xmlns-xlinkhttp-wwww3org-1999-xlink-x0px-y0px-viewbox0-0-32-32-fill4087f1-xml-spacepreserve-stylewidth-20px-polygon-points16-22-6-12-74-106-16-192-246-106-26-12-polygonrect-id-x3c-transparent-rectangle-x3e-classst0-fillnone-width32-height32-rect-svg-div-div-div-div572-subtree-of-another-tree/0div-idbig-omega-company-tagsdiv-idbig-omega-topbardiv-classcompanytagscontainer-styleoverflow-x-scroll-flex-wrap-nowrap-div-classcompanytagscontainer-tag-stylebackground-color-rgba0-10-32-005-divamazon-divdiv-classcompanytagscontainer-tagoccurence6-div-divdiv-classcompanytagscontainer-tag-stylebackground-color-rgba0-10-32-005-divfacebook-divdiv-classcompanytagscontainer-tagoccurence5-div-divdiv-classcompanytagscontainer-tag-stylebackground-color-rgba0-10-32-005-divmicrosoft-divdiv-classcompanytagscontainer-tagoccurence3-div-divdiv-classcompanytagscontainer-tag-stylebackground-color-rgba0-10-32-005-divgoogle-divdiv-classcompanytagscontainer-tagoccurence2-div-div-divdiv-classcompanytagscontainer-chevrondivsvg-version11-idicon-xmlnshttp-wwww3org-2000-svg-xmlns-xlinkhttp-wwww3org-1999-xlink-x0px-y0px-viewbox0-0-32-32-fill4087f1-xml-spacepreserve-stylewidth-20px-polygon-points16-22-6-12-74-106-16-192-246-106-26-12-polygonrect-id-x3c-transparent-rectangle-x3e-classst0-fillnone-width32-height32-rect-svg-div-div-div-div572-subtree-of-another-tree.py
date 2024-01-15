# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        def same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val==q.val:
                return same(p.left,q.left) and same(p.right,q.right)
            else:
                return False
        if root.val==subRoot.val:
            if same(root,subRoot):
                return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)