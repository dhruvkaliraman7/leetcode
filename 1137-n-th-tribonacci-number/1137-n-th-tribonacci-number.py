class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n==2:
            return 1
        one , two , three = 0 , 1 , 1
        tmp = 3 
        while tmp < n:
            one , two , three = two , three , one + two + three
            tmp += 1
        # print(one,two)
        return one + two + three