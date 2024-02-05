class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1 for i in range(len(arr))]
        maxn=-1
        for i in range(len(arr)-2,-1,-1):
            maxn=max(maxn,arr[i+1])
            res[i]=maxn
        return res