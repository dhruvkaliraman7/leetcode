# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.val=0
        self.dic=defaultdict(int)
        def dfs(node):
            self.dic[node.val]+=1
            if not node.left and not node.right:
                count=0
                for key in self.dic:
                    if self.dic[key]%2==1 and count>=1:
                        self.dic[node.val]-=1
                        return
                    elif self.dic[key]%2==1:
                        count+=1
                self.dic[node.val]-=1
                self.val+=1
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.dic[node.val]-=1
            return
        dfs(root)
        return self.val
            