class Solution:
    def minOperations(self, s: str) -> int:
        count1,count2=0,0
        for i,st in enumerate(s):
            if i%2==0:
                if st=='0':
                    count1+=1
                else:
                    count2+=1
            else:
                if st=='1':
                    count1+=1
                else:
                    count2+=1
        return min(count1,count2)