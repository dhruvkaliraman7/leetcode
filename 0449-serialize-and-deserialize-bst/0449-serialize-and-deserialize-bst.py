# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        lis= []
        def dfs(node):
            if not node:
                lis.append('N')
                return
            lis.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(lis)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        tmp = data.split(',')
        self.ind = 0
        def dfs():
            if tmp[self.ind] == 'N':
                self.ind += 1
                return None
            node = TreeNode(int(tmp[self.ind]))
            self.ind+=1
            node.left = dfs()
            node.right = dfs()
            return node 
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans