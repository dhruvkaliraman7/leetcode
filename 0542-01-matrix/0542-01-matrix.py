class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r , c = len(mat) , len(mat[0])
        dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        new_grid = [[-1 for _ in range(c)] for _ in range(r)]
        q=collections.deque()
        visit= set()
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        count=0
        while q:
            for i in range(len(q)):
                tmp_loc = q.popleft()
                new_grid[tmp_loc[0]][tmp_loc[1]] = count
                for new_r,new_c in dirs:
                    comp_x, comp_y = new_r+tmp_loc[0] , new_c +tmp_loc[1]
                    if comp_x <0 or comp_y < 0 or comp_x >=r or comp_y >= c or (comp_x,comp_y) in visit:
                        continue
                    q.append((comp_x,comp_y))
                    visit.add((comp_x,comp_y))
            count+=1
        return new_grid
                    
                
            