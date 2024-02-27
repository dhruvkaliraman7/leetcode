class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic=defaultdict(int)
        for t in text:
            dic[t]+=1
        # print(dic)
        return min(dic['b'],dic['a'],dic['l']//2,dic['o']//2,dic['n'])