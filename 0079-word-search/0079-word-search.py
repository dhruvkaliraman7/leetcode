class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        r,c=len(board),len(board[0])
        def dfs(board,r,c,visit,numb):
            if r<0 or c<0 or r>=len(board) or c >=len(board[0]) or board[r][c]!=word[numb] or (r,c) in visit:
                return False
            
            numb+=1
            if numb==len(word):
                return True
            tmp=False
            visit.add((r,c))
            for r_,c_ in dirs:
                tmp =dfs(board,r+r_,c+c_,visit,numb) or tmp
            if not tmp:
                numb-=1
                visit.remove((r,c))
            
            return tmp
        for i in range(r):
            for j in range(c):
                tmp= dfs(board,i,j,set(),0)
                if tmp==True:
                    return True
        return False