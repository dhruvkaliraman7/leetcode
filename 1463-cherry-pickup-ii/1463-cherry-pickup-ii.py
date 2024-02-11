class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp={}
        r,c=len(grid),len(grid[0])
        dirs=[(1,0),(1,-1),(1,1)]
        def dfs(rx1,ry1,ry2):
            if ry1<0 or ry2<0 or ry1>=c or ry2>=c:
                return 0
            if (rx1,ry1,ry2) in dp:
                return dp[rx1,ry1,ry2]
            if rx1==r-1:
                if ry1==ry2:
                    return grid[rx1][ry1] 
                return grid[rx1][ry1]+grid[rx1][ry2]
            tmp=0
            if ry1==ry2:
                reward=grid[rx1][ry1]
            else:
                reward=grid[rx1][ry1]+grid[rx1][ry2]
            for x1,y1 in dirs:
                for x2,y2 in dirs:
                    tmp=max(tmp,dfs(rx1+1,ry1+y1,ry2+y2))
            dp[(rx1,ry1,ry2)]= tmp+reward
            return dp[(rx1,ry1,ry2)]
        return dfs(0,0,c-1)