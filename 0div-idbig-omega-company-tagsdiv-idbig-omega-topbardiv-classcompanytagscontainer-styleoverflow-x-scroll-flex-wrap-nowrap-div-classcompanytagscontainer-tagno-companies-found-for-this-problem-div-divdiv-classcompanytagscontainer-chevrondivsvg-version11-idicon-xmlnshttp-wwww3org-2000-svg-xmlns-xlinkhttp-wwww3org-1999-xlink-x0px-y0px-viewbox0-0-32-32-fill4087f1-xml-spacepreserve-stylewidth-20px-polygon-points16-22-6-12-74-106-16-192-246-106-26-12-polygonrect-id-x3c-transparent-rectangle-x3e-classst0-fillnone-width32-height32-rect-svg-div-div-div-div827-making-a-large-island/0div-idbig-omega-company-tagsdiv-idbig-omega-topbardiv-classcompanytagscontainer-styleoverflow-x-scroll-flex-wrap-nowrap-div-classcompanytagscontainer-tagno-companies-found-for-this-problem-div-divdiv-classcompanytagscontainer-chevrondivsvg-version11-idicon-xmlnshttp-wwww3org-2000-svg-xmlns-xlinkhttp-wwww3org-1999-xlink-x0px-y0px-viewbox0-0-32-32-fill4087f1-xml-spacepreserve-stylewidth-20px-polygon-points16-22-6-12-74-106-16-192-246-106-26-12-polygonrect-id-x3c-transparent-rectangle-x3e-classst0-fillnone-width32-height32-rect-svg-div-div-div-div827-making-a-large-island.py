class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dic=defaultdict(int)
        start=2
        r,c=len(grid),len(grid[0])
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(num,i,j):
            if i<0 or j<0 or j>=c or i>=r or (i,j) in visit or grid[i][j]==0:
                return 0
            tmp=1
            visit.add((i,j))
            grid[i][j]=num
            for new_i,new_j in dirs:
                tmp+=dfs(num,i+new_i,j+new_j)
            
            return tmp
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    visit=set()
                    dic[start]=dfs(start,i,j)
                    start+=1
        maxn=0
        if dic.values():
            maxn=max(dic.values())
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    tmp=1
                    a=set()
                    for dir_i,dir_j in dirs:
                        if i+dir_i<0 or j+dir_j<0 or j+dir_j>=c or i+dir_i>=r or grid[i+dir_i][j+dir_j] in a:
                            continue
                        tmp+=dic[grid[i+dir_i][j+dir_j]]
                        a.add(grid[i+dir_i][j+dir_j])
                        
                    maxn=max(maxn,tmp)
        return maxn