class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie={}
        def insert(word):
            tmp=self.trie
            for ch in word:
                if ch not in tmp:
                    tmp[ch]={}
                tmp=tmp[ch]
            tmp['*']=''
        
        for word in words:
            insert(word)
            
        res=set()
        r,c=len(board),len(board[0])
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j,dic,tmp_str,visit):
            if i<0 or j<0 or i>=r or j>=c or (i,j) in visit or board[i][j] not in dic:
                return 
            
            if '*' in dic[board[i][j]]:
                res.add(tmp_str+board[i][j])
                
            
            visit.add((i,j))
            for new_r,new_c in dirs:
                dfs(i+new_r, j+new_c,dic[board[i][j]],tmp_str+board[i][j],visit)
            visit.remove((i,j))
        for i in range(r):
            for j in range(c):
                dfs(i,j,self.trie,'',set())
        return list(res)
            
        
            