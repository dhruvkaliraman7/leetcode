class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid=[[0 for i in range(n)]for _ in range(n)]
        rowu,rowd=0,len(grid)-1
        coll,colr=0,len(grid[0])-1
        count=0
        r,c=len(grid),len(grid[0])
        while r*c>count:
            # print(count)
            for i in range(coll,colr+1):
                grid[rowu][i]=count+1
                count+=1
            for i in range(rowu+1,rowd+1):
                grid[i][colr]=count+1
                count+=1
            if rowu<rowd:
                for i in range(colr-1,coll-1,-1):
                    grid[rowd][i]=count+1
                    count+=1
            if coll<colr:    
                for i in range(rowd-1,rowu,-1):
                    grid[i][coll]=count+1
                    count+=1
            rowu+=1
            rowd-=1
            coll+=1
            colr-=1
            # print(count)
            # print(r*c)
            # break
        return grid
        