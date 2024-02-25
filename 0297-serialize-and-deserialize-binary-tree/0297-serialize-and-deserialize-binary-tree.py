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
        self.st=[]
        def dfs(node):
            if not node:
                self.st.append('N')
                return
            self.st.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        # print(self.st)
        self.st=','.join(self.st)
        return self.st
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        new_lis=data.split(',')
        self.i=0
        def dfs():
            if self.i>=len(new_lis):
                return None
            if new_lis[self.i]=='N':
                self.i+=1
                return None
            node=TreeNode(int(new_lis[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))