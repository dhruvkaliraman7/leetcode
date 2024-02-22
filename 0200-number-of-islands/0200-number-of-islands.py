class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        r,c=len(grid),len(grid[0])
        def dfs(x,y):
            if x<0 or y<0 or x>=r or y>=c or grid[x][y]=='0':
                return 
            grid[x][y]='0'
            for new_x,new_y in dirs:
                dfs(x+new_x,y+new_y)
            
            
        
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count