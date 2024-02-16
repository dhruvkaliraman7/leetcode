class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        count=[]
        spiral=1
        tmp_r,tmp_c=rStart,cStart
        
        def check(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return False
            return True
        j=0
        while len(count)!=rows*cols:
            for i in range(tmp_c,tmp_c+spiral):
                if check(tmp_r,i):
                    count.append([tmp_r,i])
            tmp_c+=spiral
            for i in range(tmp_r,tmp_r+spiral):
                if check(i,tmp_c):
                    count.append([i,tmp_c])
            tmp_r+=spiral
            spiral+=1
            for i in range(tmp_c,tmp_c-spiral,-1):
                if check(tmp_r,i):
                    count.append([tmp_r,i])
            tmp_c-=spiral
            for i in range(tmp_r,tmp_r-spiral,-1):
                if check(i,tmp_c):
                    count.append([i,tmp_c])
            tmp_r-=spiral
            spiral+=1
            # j+=1
            # if j==100:
            #     break
            # print(count)
            # print(rows*cols)
        return count
            