class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=1
        tmp_sum=0
        cont_flag=False
        res=0
        tot_sum=neededTime[0]
        tmp_sum=neededTime[0]
        while i<len(colors):

            if colors[i]==colors[i-1]:
                tmp_sum=max(tmp_sum,neededTime[i])
                tot_sum+=neededTime[i]
                cont_flag=True
            else:
                if cont_flag:
                    res+=tot_sum-tmp_sum
                tmp_sum=neededTime[i]
                tot_sum=neededTime[i]
            i+=1
        if cont_flag:
            res+=tot_sum-tmp_sum
        return res