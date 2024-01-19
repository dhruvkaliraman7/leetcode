class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r,c=len(matrix),len(matrix[0])
        dirs=[(1,1),(1,-1),(1,0)]
        dp={}
        def dfs(x,y):
            if (x,y) in dp:
                return dp[(x,y)]
            if x==len(matrix)-1 and y>=0 and y<c:
                return matrix[x][y]
            tmp=float('inf')
            for dir_r,dir_c in dirs:
                new_r,new_c=dir_r+x,dir_c+y
                if new_r<0 or new_c<0 or new_r>=r or new_c>=c:
                    continue
                tmp=min(tmp,matrix[x][y]+dfs(new_r,new_c))
            dp[(x,y)]=tmp
            return dp[(x,y)]
        res=[]
        for i in range(len(matrix[0])):
            res.append(dfs(0,i))
        return min(res)