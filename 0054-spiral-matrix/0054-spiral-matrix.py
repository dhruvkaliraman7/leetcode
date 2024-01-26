class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.arr=[]
        self.visit=set()
        r,c=len(matrix),len(matrix[0])
        def dfs(x,y,mode):
            #print(x,y)
            if x<0 or x>=r or y<0 or y>=c:
                return
            if (x,y) in self.visit:
                return
            if mode=='r':
                if (x,y) not in self.visit:
                    self.visit.add((x,y))
                self.arr.append(matrix[x][y])
                if y==c-1 or (x,y+1) in self.visit:
                    if x+1==r:
                        return
                    dfs(x+1,y,'d')
                else:
                    dfs(x,y+1,'r')
            if mode=='d':
                if (x,y) not in self.visit:
                    self.visit.add((x,y))
                self.arr.append(matrix[x][y])
                if x==r-1 or (x+1,y) in self.visit:
                    if y-1==c:
                        return
                    dfs(x,y-1,'l')
                else:
                    dfs(x+1,y,'d')
            if mode=='l':
                if (x,y) not in self.visit:
                    self.visit.add((x,y))
                self.arr.append(matrix[x][y])
                if y==0 or (x,y-1) in self.visit:
                    if x-1==r:
                        return
                    dfs(x-1,y,'u')
                else:
                    dfs(x,y-1,'l')
            if mode=='u':
                if (x,y) not in self.visit:
                    self.visit.add((x,y))
                self.arr.append(matrix[x][y])
                if x==1 or (x-1,y) in self.visit:
                    if y+1==c:
                        return
                    dfs(x,y+1,'r')
                else:
                    dfs(x-1,y,'u')
        dfs(0,0,'r')
        return self.arr
        