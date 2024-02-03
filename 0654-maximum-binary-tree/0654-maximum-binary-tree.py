# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def func(arr):
            if not arr:
                return None
            min_ind,max_val=-1,-1
            for i,ele in enumerate(arr):
                if ele>max_val:
                    max_val=ele
                    min_ind=i
            tmp=TreeNode(max_val)
            tmp.left=func(arr[:min_ind])
            tmp.right=func(arr[min_ind+1:])
            return tmp
        return func(nums)
        