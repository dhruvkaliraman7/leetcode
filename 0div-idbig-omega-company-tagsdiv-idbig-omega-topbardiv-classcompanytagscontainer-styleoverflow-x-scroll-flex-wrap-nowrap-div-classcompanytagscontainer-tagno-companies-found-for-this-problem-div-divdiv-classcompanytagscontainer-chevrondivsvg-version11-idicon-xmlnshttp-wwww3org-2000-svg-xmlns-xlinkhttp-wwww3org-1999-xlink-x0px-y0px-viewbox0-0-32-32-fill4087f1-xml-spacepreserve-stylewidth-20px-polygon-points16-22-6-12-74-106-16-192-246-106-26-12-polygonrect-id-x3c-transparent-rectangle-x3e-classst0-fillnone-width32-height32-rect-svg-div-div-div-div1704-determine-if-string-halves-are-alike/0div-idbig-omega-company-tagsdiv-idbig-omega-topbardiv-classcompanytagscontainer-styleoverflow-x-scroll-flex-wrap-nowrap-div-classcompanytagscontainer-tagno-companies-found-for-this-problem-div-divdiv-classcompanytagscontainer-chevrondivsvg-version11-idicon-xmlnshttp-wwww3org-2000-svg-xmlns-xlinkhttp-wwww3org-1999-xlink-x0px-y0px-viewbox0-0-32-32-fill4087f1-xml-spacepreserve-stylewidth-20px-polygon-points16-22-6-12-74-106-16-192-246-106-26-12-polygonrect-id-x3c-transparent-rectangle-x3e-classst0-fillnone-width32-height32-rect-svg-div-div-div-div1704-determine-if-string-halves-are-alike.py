class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lenn=len(s)//2
        a=set()
        a.add('a')
        a.add('e')
        a.add('i')
        a.add('o')
        a.add('u')
        a.add('A')
        a.add('E')
        a.add('I')
        a.add('O')
        a.add('U')
        l=0
        for i in range(lenn):
            if s[i] in a:
                l+=1
        for i in range(lenn, len(s)):
            if s[i] in a:
                l-=1
        return l==0