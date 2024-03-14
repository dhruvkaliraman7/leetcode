class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col = set(),set()
        r,c = len(matrix),len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for ele in row:
            for i in range(c):
                matrix[ele][i] = 0
        for ele in col:
            for i in range(r):
                matrix[i][ele] = 0
        return matrix