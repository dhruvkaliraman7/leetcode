# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heapArray = []
        heapq.heapify(heapArray)
        def dfs(node):
            if not node:
                return
            if len(heapArray) <= k:
                if len(heapArray) < k:
                    heapq.heappush(heapArray, -node.val)    
                elif node.val < -heapArray[0] :
                    heapq.heappop(heapArray)
                    heapq.heappush(heapArray, -node.val)    
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        return -heapArray[0]