class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.tot_count=0
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        dp={}
        def dfs(x,y,moves):
            if (x,y,moves) in dp:
                return dp[(x,y,moves)]
            if x<0 or y<0 or x>=m or y>=n:
                #print(x,y,moves)
                if moves<=maxMove:
                    return 1
                return 0
            if moves==maxMove:
                return 0
            tmp=0
            for new_x,new_y in dirs:
                tmp+=dfs(x+new_x,y+new_y,moves+1)
            dp[(x,y,moves)]=tmp
            return tmp
            
        return dfs(startRow,startColumn,0)%(10**9+7)
        
                    