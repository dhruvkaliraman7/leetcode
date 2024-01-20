class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        sumn=0
        i=0
        while i<len(s):
            if s[i]=='(':
                stack.append('(')
            elif s[i]==')':
                tmp_sum=0
                while stack and stack[-1]!='(':
                    tmp=stack.pop()
                    tmp_sum+=tmp
                if stack[-1]=='(':
                    stack.pop()
                    if tmp_sum==0:
                        stack.append(1+tmp_sum)
                    else:
                        stack.append(tmp_sum*2)
            i+=1
        return sum(stack)