class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        maxn = 0
        dic = {}
        for i,num in enumerate(nums):
            if num not in dic:
                dic[num] = [1,i,i]
            else:
                tmp = dic[num]
                dic[num] = [tmp[0]+1, tmp[1], i]
            maxn = max(maxn, dic[num][0])
        num = float('inf')
        # print(dic)
        for k in dic:
            if dic[k][0] == maxn:
                num = min(num, dic[k][2]- dic[k][1])
        return num + 1