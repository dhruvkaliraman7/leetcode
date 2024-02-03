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
            tmp=TreeNode(max(arr))
            tmp.left=func(arr[:arr.index(max(arr))])
            tmp.right=func(arr[arr.index(max(arr))+1:])
            return tmp
        return func(nums)
        