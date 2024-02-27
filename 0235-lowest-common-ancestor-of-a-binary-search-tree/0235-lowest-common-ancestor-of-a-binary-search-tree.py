# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node.val == p.val:
                return p
            if node.val == q.val:
                return q
            
            p1 , q1 = None , None
            if node.right:
                p1 = dfs(node.right)
            
            if node.left:
                q1 = dfs(node.left)
            
            if p1 and q1:
                return node
            else:
                return p1 or q1
        return dfs(root)
        
                