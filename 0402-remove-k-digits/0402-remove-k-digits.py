class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=k:
            return "0"
        stack=[]
        for i in range(len(num)):
            if not stack:
                stack.append(num[i])
            else:
                while k>0 and stack:
                    if num[i]<stack[-1]:
                        stack.pop()
                        k-=1
                    else:
                        break
                stack.append(num[i])        
        for i in range(k):
            stack.pop()
        flag=False
        tmp_str=''
        for n in stack:
            if not flag and n=='0':
                continue
            else:
                tmp_str+=n
                flag=True
        
        return tmp_str if tmp_str!='' else '0'