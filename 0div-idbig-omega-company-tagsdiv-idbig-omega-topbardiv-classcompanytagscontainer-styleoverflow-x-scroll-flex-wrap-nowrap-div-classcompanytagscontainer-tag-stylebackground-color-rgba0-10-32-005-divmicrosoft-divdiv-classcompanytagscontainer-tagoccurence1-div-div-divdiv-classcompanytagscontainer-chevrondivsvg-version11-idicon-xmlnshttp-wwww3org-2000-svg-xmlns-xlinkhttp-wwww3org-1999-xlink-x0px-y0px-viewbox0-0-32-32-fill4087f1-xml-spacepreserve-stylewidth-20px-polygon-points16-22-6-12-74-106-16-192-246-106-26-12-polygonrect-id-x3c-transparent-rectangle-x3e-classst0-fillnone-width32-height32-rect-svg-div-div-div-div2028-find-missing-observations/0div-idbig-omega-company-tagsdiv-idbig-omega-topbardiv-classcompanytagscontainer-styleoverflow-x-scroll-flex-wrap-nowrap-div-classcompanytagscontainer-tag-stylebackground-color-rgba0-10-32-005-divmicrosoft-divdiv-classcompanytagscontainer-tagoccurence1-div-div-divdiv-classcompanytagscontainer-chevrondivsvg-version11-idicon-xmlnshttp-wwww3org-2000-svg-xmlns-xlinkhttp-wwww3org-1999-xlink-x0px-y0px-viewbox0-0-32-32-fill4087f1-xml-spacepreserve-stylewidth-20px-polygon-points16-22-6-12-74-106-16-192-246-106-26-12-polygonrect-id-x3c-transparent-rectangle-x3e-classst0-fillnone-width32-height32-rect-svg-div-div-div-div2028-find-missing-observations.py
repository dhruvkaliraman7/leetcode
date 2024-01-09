class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumn=sum(rolls)
        target=(mean*(len(rolls)+n))-sumn
        print(target)
        if target/n>6 or target/n<0:
            return []
        res=[0 for i in range(n)]
        for i in range(6):
            for j in range(len(res)):
                if target==0:
                    if 0 in res:
                        return []
                    return res
                res[j]+=1
                target-=1
        return res
                