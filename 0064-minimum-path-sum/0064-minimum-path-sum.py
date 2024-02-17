class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        r,c=len(grid),len(grid[0])
        def dfs(i,j):
            if i>=r or j>=c:
                return float('inf')
            if i==r-1 and j==c-1:
                return grid[i][j]
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)]=grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
            return dp[(i,j)]
        return dfs(0,0)