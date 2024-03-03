class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = defaultdict(int)
        for st in s:
            dic[st] += 1
        stack = []
        for st in s:
            if not stack:
                stack.append(st)
            else:
                while stack and st not in stack and ord(stack[-1])> ord(st) and dic[stack[-1]]>1:
                    dic[stack[-1]]-=1
                    stack.pop()
                if st not in stack:
                    stack.append(st)
                else:
                    dic[st]-=1
        return ''.join(stack)