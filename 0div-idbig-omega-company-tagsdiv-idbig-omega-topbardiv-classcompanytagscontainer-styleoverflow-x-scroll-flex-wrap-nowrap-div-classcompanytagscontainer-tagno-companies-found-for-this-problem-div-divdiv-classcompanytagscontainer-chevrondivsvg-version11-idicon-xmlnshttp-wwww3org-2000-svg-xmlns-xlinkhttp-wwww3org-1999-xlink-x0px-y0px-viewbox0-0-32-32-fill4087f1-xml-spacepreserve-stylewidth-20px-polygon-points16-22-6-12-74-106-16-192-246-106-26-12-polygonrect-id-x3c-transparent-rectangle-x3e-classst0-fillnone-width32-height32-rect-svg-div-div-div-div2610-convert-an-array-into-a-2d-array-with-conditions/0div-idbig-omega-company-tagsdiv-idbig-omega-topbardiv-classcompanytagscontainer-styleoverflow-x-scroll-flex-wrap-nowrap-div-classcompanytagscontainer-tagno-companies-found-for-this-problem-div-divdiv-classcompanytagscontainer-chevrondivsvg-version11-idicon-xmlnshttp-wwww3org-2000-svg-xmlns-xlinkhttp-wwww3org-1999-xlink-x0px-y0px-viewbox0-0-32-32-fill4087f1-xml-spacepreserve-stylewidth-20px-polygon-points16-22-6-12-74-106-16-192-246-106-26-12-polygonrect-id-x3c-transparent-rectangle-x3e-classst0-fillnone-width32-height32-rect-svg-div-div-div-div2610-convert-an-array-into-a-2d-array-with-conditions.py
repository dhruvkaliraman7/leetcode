class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic=defaultdict(int)
        for n in nums:
            dic[n]+=1
        mat=[[] for i in range(max(dic.values()))]
        for key in dic.keys():
            i=0
            while dic[key]>0:
                mat[i].append(key)
                dic[key]-=1
                i+=1
        return mat