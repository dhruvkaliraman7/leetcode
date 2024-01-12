class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        flag=True
        first,second=[],[]
        maxn=float("-inf")
        for n in nums:
            if n==0:
                flag=True
                first.append(0)
            else:
                if flag==True:
                    flag=False
                    first.append(n)
                else:
                    first.append(n*first[-1])
            maxn=max(maxn,first[-1])
        flag=True
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                flag=True
                second.append(0)
            else:
                if flag==True:
                    flag=False
                    second.append(nums[i])
                else:
                    second.append(nums[i]*second[-1])
            maxn=max(maxn,second[-1])
        return maxn
                
                