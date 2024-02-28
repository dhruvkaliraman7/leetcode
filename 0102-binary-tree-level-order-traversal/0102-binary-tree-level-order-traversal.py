# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=collections.deque([root])
        fin=[]
        while q:
            tmp_list=[]
            for i in range(len(q)):
                tmp=q.popleft()
                tmp_list.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            fin.append(tmp_list)
        return fin