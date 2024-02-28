class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        start=colors[0]
        cur_sum=neededTime[0]
        tmp_max=cur_sum
        res=0
        for i in range(1,len(colors)):
            if colors[i]==start:
                cur_sum+=neededTime[i]
                tmp_max=max(tmp_max,neededTime[i])
            else:
                start=colors[i]
                res+=(cur_sum-tmp_max)
                tmp_max=neededTime[i]
                cur_sum=neededTime[i]
        res+=(cur_sum-tmp_max)
        return res