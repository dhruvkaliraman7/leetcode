class Solution:
    def climbStairs(self, n: int) -> int:
        zero,one=1,1
        while n>1:
            tmp=one
            one=one+zero
            zero=tmp
            n-=1
        return one