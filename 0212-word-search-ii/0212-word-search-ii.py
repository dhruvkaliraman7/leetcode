class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = {}
        self.res = set()
        def addWord(word,mapTrie):
            for w in word:
                if w not in mapTrie:
                    mapTrie[w]={}
                mapTrie = mapTrie[w]    
            mapTrie['#']='#'
            return
        for word in words:
            addWord(word,self.trie)
        r,c =len(board), len(board[0])
        
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(i,j,visit,trie,curWord):
            if '#' in trie:
                self.res.add(curWord)
            if 0<=i<r and 0<=j<c and (i,j) not in visit and board[i][j] in trie:
                visit.add((i,j))
                # curWord += grid[i][j] 
                for newX,newY in dirs:
                    dfs(i+newX,j+newY,visit,trie[board[i][j]],curWord+board[i][j] )
                visit.remove((i,j))
                    
        for i in range(r):
            for j in range(c):
                if board[i][j] in self.trie:
                    dfs(i,j,set(),self.trie,'')
        return list(self.res)
                    