class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zero_coor=set()
        two_coor=set()
        r,c=len(grid),len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    zero_coor.add((i,j))
                elif grid[i][j]>1:
                    two_coor.add((i,j))
        
        def backtrak():
            if not zero_coor:
                return 0
            min_cost=float('inf')
            for z_x,z_y in zero_coor:
                zero_coor.remove((z_x,z_y))
                for two_x,two_y in two_coor:
                    if grid[two_x][two_y]>1:
                        grid[two_x][two_y]-=1
                        min_cost=min(min_cost,abs(z_x-two_x)+abs(z_y-two_y)+backtrak())
                        grid[two_x][two_y]+=1
                zero_coor.add((z_x,z_y))
            return min_cost
            
            
            
            
            
            
            
        return backtrak()
        