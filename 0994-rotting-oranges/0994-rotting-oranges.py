class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        num_fresh = 0
        tmp = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    num_fresh+=1
                if grid[i][j] ==2:
                    tmp.append((i,j))
        level = 0
        tmp.append((-1,-1))
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        while tmp:
            
            tmpNode = tmp.popleft()
            # print(tmp)
            if tmpNode[0] == -1:
                if not tmp:
                    if num_fresh == 0:
                        return level
                    return -1
                tmp.append((-1,-1))
                level +=1
            else:
                for x,y in dirs:
                    if 0<=x+tmpNode[0]<r and 0<=y+tmpNode[1]<c:
                        if grid[x+tmpNode[0]][y+tmpNode[1]] == 1:
                            tmp.append((x+tmpNode[0],y+tmpNode[1]))
                            num_fresh -= 1
                            grid[x+tmpNode[0]][y+tmpNode[1]] = 0
        
                