class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        grid=[set() for i in range(9)]
        
        r,c=len(board),len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j]=='.':
                    continue
                rowl=len(rows[i])
                coll=len(cols[j])
                gridl=len(grid[i//3*3+j//3])
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[i//3*3+j//3].add(board[i][j])
                if rowl==len(rows[i]) or coll==len(cols[j]) or gridl==len(grid[i//3*3+j//3]):
                    return False
        return True