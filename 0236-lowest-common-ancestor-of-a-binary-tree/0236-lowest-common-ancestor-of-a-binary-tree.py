# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node==p or node==q:
                return node
            l,r = None, None
            if node.left:
                l=lca(node.left)
            if node.right:
                r=lca(node.right)
            if l and r:
                return node
            if l or r:
                return l or r
            # return None
        return lca(root)