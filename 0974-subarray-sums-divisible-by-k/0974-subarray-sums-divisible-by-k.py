class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        forw,back=defaultdict(int),defaultdict(int)
        sumn=0
        for n in nums:
            sumn+=n
            forw[sumn%k]+=1
        # for i in range(len(nums)-1,-1,-1):
        #     back[n%k]+=1
        res=0
        #print(forw)
        for key in forw:
            if key==0:
                res+=forw[key]
                
            
            res+=(forw[key]*(forw[key]-1))/2
        # for key in back:
        #     if key==0:
        #         res+=back[key]
        #     else:
        #         res+=back[key]-1
        return int(res)
        