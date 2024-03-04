class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i=0
        stack=[]
        prev=''
        while i<len(s):
            if prev==s[i]:
                tmp=stack.pop()
                re_k=tmp[1]+1
                if re_k>=k:
                    if stack:
                        prev=stack[-1][0]
                    else:
                        prev=None
                else:
                    stack.append((tmp[0],re_k))
            else:
                stack.append((s[i],1))
                prev=s[i]
            i+=1
        fin=''
        for a,b in stack:
            fin=fin+a*b
        return fin