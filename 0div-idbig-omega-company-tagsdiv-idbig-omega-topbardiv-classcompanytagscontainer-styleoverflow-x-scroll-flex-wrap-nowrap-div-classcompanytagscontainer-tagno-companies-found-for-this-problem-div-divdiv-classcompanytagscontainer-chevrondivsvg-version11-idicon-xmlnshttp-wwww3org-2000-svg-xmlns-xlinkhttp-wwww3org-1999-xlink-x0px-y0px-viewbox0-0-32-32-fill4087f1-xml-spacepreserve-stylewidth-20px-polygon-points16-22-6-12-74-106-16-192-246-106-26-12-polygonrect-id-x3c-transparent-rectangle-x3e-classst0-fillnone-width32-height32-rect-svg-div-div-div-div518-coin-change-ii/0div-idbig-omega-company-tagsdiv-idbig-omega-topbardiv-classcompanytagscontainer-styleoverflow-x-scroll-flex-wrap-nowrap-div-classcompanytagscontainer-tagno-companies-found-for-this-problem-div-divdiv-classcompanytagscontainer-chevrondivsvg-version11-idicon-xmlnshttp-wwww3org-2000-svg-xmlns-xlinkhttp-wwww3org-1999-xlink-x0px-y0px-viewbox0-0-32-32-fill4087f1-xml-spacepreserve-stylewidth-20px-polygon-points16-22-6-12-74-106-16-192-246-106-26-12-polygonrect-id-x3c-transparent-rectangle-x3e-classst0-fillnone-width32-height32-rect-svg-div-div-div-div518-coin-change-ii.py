class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res=[[0 for i in range(amount+1)]for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            res[i][0]=1
        for j in range(0,len(coins)):
            for i in range(1,amount+1):
                if coins[j]>i:
                    res[j+1][i]=res[j][i]
                else:
                    res[j+1][i]=res[j][i]+res[j+1][i-coins[j]]
        return res[len(coins)][amount]
                    