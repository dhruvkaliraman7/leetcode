class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for word in strs:
            tmp=''.join(sorted(word))
            #print(word)
            #print(tmp)
            dic[tmp].append(word)
        res=[]
        for values in dic.values():
            res.append(values)
        return res