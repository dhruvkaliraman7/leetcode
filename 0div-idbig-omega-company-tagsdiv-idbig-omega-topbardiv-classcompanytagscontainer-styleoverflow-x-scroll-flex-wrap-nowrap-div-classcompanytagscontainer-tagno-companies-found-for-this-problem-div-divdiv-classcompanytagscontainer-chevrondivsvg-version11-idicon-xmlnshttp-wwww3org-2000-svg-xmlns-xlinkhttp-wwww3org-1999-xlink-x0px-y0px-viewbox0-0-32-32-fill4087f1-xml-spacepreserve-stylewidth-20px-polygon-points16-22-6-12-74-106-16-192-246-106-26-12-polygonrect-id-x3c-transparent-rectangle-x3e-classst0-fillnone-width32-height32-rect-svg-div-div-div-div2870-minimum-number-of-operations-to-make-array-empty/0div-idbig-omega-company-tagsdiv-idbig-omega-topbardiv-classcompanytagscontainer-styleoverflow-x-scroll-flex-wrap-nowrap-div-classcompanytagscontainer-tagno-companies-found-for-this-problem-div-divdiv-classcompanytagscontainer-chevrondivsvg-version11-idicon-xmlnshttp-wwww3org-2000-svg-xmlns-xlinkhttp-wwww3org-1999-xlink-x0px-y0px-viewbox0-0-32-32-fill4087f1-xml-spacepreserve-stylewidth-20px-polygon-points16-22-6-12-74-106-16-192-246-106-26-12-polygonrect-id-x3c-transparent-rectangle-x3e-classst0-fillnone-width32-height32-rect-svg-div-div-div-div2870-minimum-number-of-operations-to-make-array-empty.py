class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for n in nums:
            dic[n]+=1
        for n in dic.values():
            if n==1:
                return -1
        res=0
        for n in dic.values():
            if n%3==0:
                res+=(n/3)
            elif n%3==1:
                res+=2
                n-=4
                res+=(n/3)
            else:
                res+=1
                n-=2
                res+=(n/3)
        return int(res)