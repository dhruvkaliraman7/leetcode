# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        tmp=-1
        def dfs(node):
            nonlocal tmp
            if node.right:
                minn_r,max_r=dfs(node.right)
            else:
                minn_r,max_r=node.val,node.val
            if node.left:
                minn_l,max_l=dfs(node.left)
            else:
                minn_l,max_l=node.val,node.val
            tmp=max(tmp,max(abs(node.val-max(max_l,max_r,node.val)),abs(node.val-min(minn_l,minn_r,node.val))))
            # if node.val==0:
            #     print((minn_l,minn_r))
            #     print((max_l,max_r))
            return min(minn_l,minn_r,node.val),max(max_l,max_r,node.val)
        dfs(root)
        return tmp