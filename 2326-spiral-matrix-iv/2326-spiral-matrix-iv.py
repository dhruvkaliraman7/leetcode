# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(m)]
        up = left = 0
        right = n -1
        down = m -1
        count = 0
        while (m*n) > count:
            for i in range(left, right+1):
                if head:
                    matrix[up][i] = head.val
                    head=head.next
                else:
                    matrix[up][i] = -1
                count+=1
            for i in range(up+1,down+1):
                if head:
                    matrix[i][right] = head.val
                    head=head.next
                else:
                    matrix[i][right] = -1
                count+=1
            
            if up!=down:
                for i in range(right-1, left-1,-1):
                    if head:
                        matrix[down][i] = head.val
                        head=head.next
                    else:
                        matrix[down][i] = -1
                    count+=1
            if right!=left:
                for i in range(down-1,up,-1):
                    if head:
                        matrix[i][left] = head.val
                        head=head.next
                    else:
                        matrix[i][left] = -1
                    count+=1
            up+=1
            right-=1
            left+=1
            down-=1
        return matrix
                