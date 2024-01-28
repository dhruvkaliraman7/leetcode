class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r,c=len(matrix),len(matrix[0])
        for i in range(r):
            for j in range(c):
                if i-1>=0 and j-1>=0:
                    matrix[i][j]=matrix[i][j]-matrix[i-1][j-1]+matrix[i-1][j]+matrix[i][j-1]
                elif i-1>=0:
                    matrix[i][j]+=matrix[i-1][j]
                elif j-1>=0:
                    matrix[i][j]+=matrix[i][j-1]
        count=0
        # print(matrix)
        for i in range(0,r):
            for j in range(i,r):
                tmp_dic=defaultdict(int)
                tmp_dic[0]=1
                if i!=j:
                   
                    tmp_arr = [x - y for x, y in zip(matrix[j], matrix[i])]

                   
                else:
                    tmp_arr=matrix[i]
                # print(tmp_dic)
                # print(tmp_arr)
                for ele in tmp_arr:
                
                    if ele-target in tmp_dic:
                        count+=tmp_dic[ele-target]
                    tmp_dic[ele]+=1
        return count

