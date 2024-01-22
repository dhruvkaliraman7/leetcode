class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        new_s=set()
        err=[]
        for n in nums:
            tmp_len=len(new_s)
            new_s.add(n)
            if tmp_len==len(new_s):
                err.append(n)
        for i in range(1,10**4+1):
            if i not in new_s:
                err.append(i)
                return err
                