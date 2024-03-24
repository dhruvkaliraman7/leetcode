class Solution:
    def minOperations(self, k: int) -> int:
        dup = 1
        inc = 1
        glo_min =k
        for i in range(1,k):
            if k%i == 0:
                glo_min = min(glo_min, k//i+i-2)
            else:
                glo_min = min(glo_min, k//i+i-1)
        return glo_min if k>1 else 0
            
            
        

