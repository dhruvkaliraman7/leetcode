class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # if sum(nums)<x:
        #     return -1
        n=len(nums)
        right_set,left_set=dic={},{}
        tmp=0
        right_set[0]=0
        left_set[0]=0
        tmp=0
        for i in range(len(nums)):
            tmp+=nums[i]
            if tmp in right_set:
                continue
            right_set[tmp]=i+1
        tmp=0
        for i in range(len(nums)-1,-1,-1):
            tmp+=nums[i]
            if tmp in left_set:
                continue
            left_set[tmp]=len(nums)-i
            
        res=float('inf')
        for key in right_set:
            if key<=x:
                if x-key in left_set and (right_set[key]+left_set[x-key])<=n:
                    res=min(res,right_set[key]+left_set[x-key])
        for key in left_set:
            if key<=x:
                if x-key in right_set and (left_set[key]+right_set[x-key])<=n:
                    res=min(res,left_set[key]+right_set[x-key])
        # print(left_set)
        # print(right_set)
        return res if res !=float('inf') else -1