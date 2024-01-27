class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        ind = inorder.index(root.val) 

        root.right = self.buildTree(inorder[ind+1:], postorder) 
        root.left = self.buildTree(inorder[:ind], postorder) 

        return root