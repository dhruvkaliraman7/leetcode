class Solution:
    def isValid(self, s: str) -> bool:
        typ=[]
        for st in s:
            # print(typ)
            if st in ['(','[','{']:
                typ.append(st)
            else:
                if typ and ((st==')' and typ[-1]=='(') or (st==']' and typ[-1]=='[') or (st=='}' and typ[-1]=='{')) :
                    typ.pop()
                else:
                    return False
            # print(typ)
        return True if not typ else False