# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.lis=[]
        def dfs(node):
            if not node:
                self.lis.append('N')
                return
            self.lis.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        a=','.join(self.lis)
        return a

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.lis=data.split(',')
        self.i=0
        # print(self.lis)
        def dfs():
            if self.lis[self.i]=='N':
                self.i+=1
                return None
            # print(self.lis[self.i])
            node=TreeNode(int(self.lis[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
    
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))