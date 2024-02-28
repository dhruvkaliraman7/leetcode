class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        dp={}
        def dfs(x,y):
            if x<0 or y<0 or x>=r or y>=c:
                return float('inf')
            if (x,y) in dp:
                return dp[(x,y)]
            if x==r-1 and y==c-1:
                return grid[x][y]
            dp[(x,y)]= grid[x][y]+min(dfs(x+1,y),dfs(x,y+1))
            return dp[(x,y)]
        return dfs(0,0)