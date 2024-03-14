class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = left = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        r,c = len(matrix) , len(matrix[0])
        res = []
        while (r*c) > len(res):
            for i in range(left,right+1):
                res.append(matrix[up][i])
            for i in range(up+1,down+1):
                res.append(matrix[i][right])
            if up!=down:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[down][i])
            if right!=left:
                for i in range(down-1,up,-1):
                    res.append(matrix[i][left])
            left += 1
            right -=1
            up +=1
            down -=1
        return res