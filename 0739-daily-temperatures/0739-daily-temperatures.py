class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[]
        for i in range(len(temperatures)-1,-1,-1):
            # print(stack)
            # print(res)
            if not stack or stack[0][0]<temperatures[i]:
                res.append(0)
                stack=[(temperatures[i],i)]
            else:
                while stack and stack[-1][0]<=temperatures[i]:
                    stack.pop()
                if stack:
                    res.append(stack[-1][1]-i)
                else:
                    res.append(0)
                stack.append((temperatures[i],i))
                
        res.reverse()
        return res
            
            
            
            
            
            
            
