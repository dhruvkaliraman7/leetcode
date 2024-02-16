class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic=defaultdict(int)
        for el in arr:
            dic[el]+=1
        tmp=[]
        for key,val in dic.items():
            tmp.append([val,key])
        heapq.heapify(tmp)
        while k>0:
            popped=heapq.heappop(tmp)
            if popped[0]<k:
                k-=popped[0]
            elif popped[0]>k:
                return len(tmp)+1
            else:
                return len(tmp)
        return len(dic.keys())
        # print(tmp)
        # return len(tmp)
        