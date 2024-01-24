class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_lis=[]
        for i in range(len(position)):
            new_lis.append([position[i],speed[i]])
        new_lis.sort(reverse=True)
        ans_lis=[]
        for i in range(len(new_lis)):
            ans_lis.append((target-new_lis[i][0])/new_lis[i][1])
        # print(new_lis)
        # print(ans_lis)
        maxn=0
        ans=0
        
        for i in range(len(ans_lis)):
            # print(ans_lis[i])
            # print(maxn)
            if ans_lis[i]<=maxn:
                continue
            else:
                maxn=ans_lis[i]
                ans+=1
        return ans
                
                