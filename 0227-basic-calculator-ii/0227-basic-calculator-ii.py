class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        i=0
        while i<len(s):
            # print(stack)
            n=s[i]
            if n==' ':
                i+=1
                continue
            elif n in ['+','-']:
                stack.append(n)
            elif n in ['/','*']:
                num1=stack.pop()
                i+=1
                # print(s[i])
                while s[i]==' ':
                    # print(s[i])
                    i+=1
                tmp=s[i]
                while i+1<len(s) and s[i+1].isdigit():
                    tmp+=s[i+1]
                    i+=1
                num2=int(tmp)
                if n=='*':
                    stack.append(num1*num2)
                else:
                    stack.append(num1//num2)
            else:
                # print(s[i])
                tmp=s[i]
                while i+1<len(s) and s[i+1].isdigit():
                    tmp+=s[i+1]
                    i+=1
                    # print(tmp)
                stack.append(int(tmp))
                
            i+=1
        t=0
        while stack:
            num1=stack.pop()
            if not stack:
                return t+num1
            sign=stack.pop()
            if sign=='+':
                t+=num1
            if sign=='-':
                t-=num1
        return num1