class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic=defaultdict(int)
        for ch in s:
            dic[ch]+=1
        stack=[]
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                while stack and ch not in stack and ord(stack[-1])>ord(ch) and dic[stack[-1]]>1:
                    dic[stack[-1]]-=1
                    stack.pop()
                if ch not in stack:
                    stack.append(ch)
                else:
                    dic[ch]-=1
        return ''.join(stack)
            
        