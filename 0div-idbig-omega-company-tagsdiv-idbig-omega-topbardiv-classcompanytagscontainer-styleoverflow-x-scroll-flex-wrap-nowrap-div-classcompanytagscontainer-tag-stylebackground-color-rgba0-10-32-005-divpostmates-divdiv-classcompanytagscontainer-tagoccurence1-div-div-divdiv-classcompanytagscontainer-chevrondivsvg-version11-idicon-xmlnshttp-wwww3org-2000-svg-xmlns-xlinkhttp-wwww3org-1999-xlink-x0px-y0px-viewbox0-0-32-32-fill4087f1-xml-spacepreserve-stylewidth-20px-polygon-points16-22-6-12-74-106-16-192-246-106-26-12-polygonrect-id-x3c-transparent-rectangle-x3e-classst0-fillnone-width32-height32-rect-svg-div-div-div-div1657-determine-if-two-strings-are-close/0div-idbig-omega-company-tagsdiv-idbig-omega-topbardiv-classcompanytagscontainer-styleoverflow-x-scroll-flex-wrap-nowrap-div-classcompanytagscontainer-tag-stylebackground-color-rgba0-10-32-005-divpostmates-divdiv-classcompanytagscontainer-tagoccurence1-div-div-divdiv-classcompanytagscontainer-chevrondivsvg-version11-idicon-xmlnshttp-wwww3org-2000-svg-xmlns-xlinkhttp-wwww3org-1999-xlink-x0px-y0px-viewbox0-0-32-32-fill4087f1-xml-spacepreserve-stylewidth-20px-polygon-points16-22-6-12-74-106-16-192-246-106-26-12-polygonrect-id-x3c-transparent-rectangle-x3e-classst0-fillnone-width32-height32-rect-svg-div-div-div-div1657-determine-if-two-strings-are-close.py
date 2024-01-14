class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic_a,dic_b=defaultdict(int),defaultdict(int)
        if len(word1)!=len(word2):
            return False
        for i in range(len(word1)):
            dic_a[word1[i]]+=1
            dic_b[word2[i]]+=1
        if dic_a.keys()!=dic_b.keys():
            return False
        return sorted(dic_a.values())==sorted(dic_b.values())