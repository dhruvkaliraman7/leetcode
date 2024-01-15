# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        glo=True
        def dfs(node):
            nonlocal glo
            if not node:
                return 0
            left,right=dfs(node.left),dfs(node.right)
            if glo:
                if abs(left-right)>1:
                    glo=False
            return 1+max(left,right)
        dfs(root)
        return glo
        