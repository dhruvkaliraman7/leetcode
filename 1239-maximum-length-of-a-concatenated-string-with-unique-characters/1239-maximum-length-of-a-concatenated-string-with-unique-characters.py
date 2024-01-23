class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dic=defaultdict(set)
        for st in arr:
            for s in st:
                tmp_len=len(dic[st])
                dic[st].add(s)
                if tmp_len==len(dic[st]):
                    del dic[st]
                    break
        res=0
        def dfs(mas_set,ind,cur_sum):
            nonlocal res
            if ind==len(arr):
                res=max(res,cur_sum)
                return
            if arr[ind] not in dic:
                return
            for ch in dic[arr[ind]]:
                if ch in mas_set:
                    res=max(res,cur_sum)
                    return 
            for ch in dic[arr[ind]]:
                mas_set.add(ch)
            for i in range(1,len(arr)-ind+1):
                dfs(mas_set,ind+i,len(mas_set))
            for ch in dic[arr[ind]]:
                mas_set.remove(ch)
        for i in range(0,len(arr)):
            dfs(set(),i,0)
        return res