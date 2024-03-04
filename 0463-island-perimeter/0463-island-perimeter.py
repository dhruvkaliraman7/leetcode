class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r , c = len(grid) , len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(x,y):
            if x<0 or y<0 or x>= r or y >= c  or grid[x][y] == 0:
                return 1
            if  (x,y) in visit:
                if grid[x][y] == 1:
                    return 0
                return 1
            tmp = 0
            visit.add((x,y))
            for new_r, new_c in dirs:
                tmp += dfs(x+new_r, y+new_c)
            return tmp
            
            
            
        visit = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    
                    return dfs(i,j)