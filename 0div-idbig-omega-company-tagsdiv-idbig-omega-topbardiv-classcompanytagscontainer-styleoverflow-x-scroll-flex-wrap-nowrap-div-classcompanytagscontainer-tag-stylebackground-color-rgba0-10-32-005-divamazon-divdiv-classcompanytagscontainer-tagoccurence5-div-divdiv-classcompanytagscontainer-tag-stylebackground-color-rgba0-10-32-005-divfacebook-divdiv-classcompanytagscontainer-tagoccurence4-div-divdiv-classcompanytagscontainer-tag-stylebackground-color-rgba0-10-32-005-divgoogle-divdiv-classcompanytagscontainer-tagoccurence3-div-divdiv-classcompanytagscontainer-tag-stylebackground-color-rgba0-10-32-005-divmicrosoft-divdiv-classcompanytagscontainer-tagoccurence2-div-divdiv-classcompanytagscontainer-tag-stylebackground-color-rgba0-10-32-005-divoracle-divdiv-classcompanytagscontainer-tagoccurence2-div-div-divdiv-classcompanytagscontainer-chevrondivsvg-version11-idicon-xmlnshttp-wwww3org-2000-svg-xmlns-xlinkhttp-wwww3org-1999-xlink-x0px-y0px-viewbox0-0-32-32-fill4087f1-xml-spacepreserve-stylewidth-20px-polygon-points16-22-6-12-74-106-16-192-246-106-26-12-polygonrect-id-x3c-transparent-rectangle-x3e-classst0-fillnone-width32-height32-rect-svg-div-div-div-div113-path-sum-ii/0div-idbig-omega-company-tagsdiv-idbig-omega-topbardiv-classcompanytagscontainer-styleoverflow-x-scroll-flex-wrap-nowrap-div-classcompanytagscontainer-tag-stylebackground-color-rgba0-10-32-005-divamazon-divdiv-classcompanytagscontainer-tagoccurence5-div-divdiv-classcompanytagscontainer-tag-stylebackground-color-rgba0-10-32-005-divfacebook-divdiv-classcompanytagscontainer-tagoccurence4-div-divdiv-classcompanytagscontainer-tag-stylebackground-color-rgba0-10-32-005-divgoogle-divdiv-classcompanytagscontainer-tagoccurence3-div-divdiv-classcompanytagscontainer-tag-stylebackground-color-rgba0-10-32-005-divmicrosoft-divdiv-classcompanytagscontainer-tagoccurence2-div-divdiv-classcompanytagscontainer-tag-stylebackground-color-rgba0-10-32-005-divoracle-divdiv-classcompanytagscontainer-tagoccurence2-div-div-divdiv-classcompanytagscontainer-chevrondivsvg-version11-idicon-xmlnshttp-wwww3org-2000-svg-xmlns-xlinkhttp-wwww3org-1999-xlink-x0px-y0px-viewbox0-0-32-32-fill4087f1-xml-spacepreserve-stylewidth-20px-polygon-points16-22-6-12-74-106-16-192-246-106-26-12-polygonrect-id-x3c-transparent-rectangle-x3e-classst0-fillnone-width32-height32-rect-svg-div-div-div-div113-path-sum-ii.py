# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(sumn,cur_path,node):
            #if node:
            #    print(sumn,cur_path,node.val)
            if not node :
                return
            if (sumn+node.val)==targetSum and not node.left and not node.right:     
                cur_path.append(node.val)
                res.append(cur_path[:])
                cur_path.pop()
                return
            
            cur_path.append(node.val)
            dfs(sumn+node.val,cur_path,node.left)
            dfs(sumn+node.val,cur_path,node.right)
            cur_path.pop()
            return
        dfs(0,[],root)
        return res