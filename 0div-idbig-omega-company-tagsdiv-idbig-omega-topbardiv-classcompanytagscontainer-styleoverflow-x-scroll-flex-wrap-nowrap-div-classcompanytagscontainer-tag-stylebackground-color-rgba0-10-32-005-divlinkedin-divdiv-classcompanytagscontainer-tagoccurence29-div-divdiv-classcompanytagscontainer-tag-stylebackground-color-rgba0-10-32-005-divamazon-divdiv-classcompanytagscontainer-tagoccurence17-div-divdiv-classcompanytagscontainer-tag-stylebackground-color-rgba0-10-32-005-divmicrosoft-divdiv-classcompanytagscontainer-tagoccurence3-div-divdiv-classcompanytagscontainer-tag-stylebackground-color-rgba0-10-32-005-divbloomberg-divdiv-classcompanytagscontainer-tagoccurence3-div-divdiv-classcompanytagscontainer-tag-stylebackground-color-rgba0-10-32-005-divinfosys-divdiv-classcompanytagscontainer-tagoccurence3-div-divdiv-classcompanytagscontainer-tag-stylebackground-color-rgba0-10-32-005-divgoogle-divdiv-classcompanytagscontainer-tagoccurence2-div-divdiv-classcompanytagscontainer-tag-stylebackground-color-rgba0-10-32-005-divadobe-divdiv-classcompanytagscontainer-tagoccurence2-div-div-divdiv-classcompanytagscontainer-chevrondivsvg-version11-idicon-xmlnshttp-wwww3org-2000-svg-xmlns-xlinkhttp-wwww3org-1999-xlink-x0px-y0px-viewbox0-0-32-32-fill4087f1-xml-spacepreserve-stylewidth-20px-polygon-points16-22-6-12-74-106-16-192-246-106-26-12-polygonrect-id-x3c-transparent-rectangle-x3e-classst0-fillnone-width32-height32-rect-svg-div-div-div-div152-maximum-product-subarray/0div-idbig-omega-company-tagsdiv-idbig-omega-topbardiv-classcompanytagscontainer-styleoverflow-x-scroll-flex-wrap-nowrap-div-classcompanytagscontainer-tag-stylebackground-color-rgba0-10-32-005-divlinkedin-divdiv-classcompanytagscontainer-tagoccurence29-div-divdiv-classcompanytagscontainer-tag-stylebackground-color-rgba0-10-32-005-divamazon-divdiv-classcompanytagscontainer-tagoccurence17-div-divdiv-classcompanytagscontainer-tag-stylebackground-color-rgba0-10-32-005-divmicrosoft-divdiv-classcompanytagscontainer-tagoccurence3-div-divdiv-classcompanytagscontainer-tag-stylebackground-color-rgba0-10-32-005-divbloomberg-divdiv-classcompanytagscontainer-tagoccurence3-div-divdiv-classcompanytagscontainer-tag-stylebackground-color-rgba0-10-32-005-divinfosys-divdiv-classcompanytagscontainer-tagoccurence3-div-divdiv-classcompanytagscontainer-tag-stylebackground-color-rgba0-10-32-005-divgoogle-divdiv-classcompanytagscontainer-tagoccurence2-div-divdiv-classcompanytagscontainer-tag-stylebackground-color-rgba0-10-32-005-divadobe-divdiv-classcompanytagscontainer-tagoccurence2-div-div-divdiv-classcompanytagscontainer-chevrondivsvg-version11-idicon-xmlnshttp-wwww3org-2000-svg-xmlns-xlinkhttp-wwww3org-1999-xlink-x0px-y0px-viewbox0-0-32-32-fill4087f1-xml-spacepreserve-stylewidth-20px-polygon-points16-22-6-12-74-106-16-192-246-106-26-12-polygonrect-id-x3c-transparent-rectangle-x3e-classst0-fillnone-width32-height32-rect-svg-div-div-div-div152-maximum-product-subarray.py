class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        flag=True
        maxn=float("-inf")
        for n in nums:
            if n==0:
                flag=True
                tmp=0
            else:
                if flag==True:
                    flag=False
                    tmp=n
                else:
                    tmp*=n
            maxn=max(maxn,tmp)
        flag=True
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                flag=True
                tmp=0
            else:
                if flag==True:
                    flag=False
                    tmp=nums[i]
                else:
                    tmp*=nums[i]
            maxn=max(maxn,tmp)
        return maxn
                
                