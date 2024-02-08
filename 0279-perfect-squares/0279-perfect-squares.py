class Solution:
    def numSquares(self, n: int) -> int:
        coin=1
        tmp=[]
        while coin**2<=n:
            tmp.append(coin**2)
            coin+=1
        res=[float('inf') for i in range(n+1)]
        res[0]=0
        for i in range(1,(n+1)):
            for coin in tmp:
                if coin<=i:
                    res[i]=min(res[i],1+res[i-coin])
        
        # print(tmp)
        # print(res)
        return res[n]