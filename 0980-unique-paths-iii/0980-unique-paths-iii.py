class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r , c = len(grid) , len(grid[0])
        startX, startY, endX, endY , count = 0 , 0, 0, 0,0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    startX, startY = i,j
                elif grid[i][j] ==2:
                    endX, endY = i,j
                elif  grid[i][j] ==0:
                    count += 1
        self.glo = 0
        # print("count", count)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(x,y, visit, tmpCount):
            # print("tmpCount", tmpCount)
            # print("x ", x)
            # print("y ", y)
            if x==endX and y==endY and tmpCount == -1:
                self.glo +=1 
                # print("tmpCoun1t", tmpCount)
                return
            if x==endX and y==endY:
                # print("tmpCount2", tmpCount)
                return
            if 0<=x<r and 0<=y<c and (x,y) not in visit and grid[x][y]!= -1:
                # print("tmpCount3", tmpCount)
                visit.add((x,y))
                new_count = tmpCount - 1 
                for newX,newY in dirs:
                    # print("new_count", new_count)
                    dfs(x+newX, y+newY,visit, new_count)
                visit.remove((x,y))
            
        
        dfs(startX, startY,set(),count)
        return self.glo
        