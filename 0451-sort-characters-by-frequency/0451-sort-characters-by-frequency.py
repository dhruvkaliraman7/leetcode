class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        
        dic_s=collections.defaultdict(int)
        for st in s:
            dic_s[st]+=1
        new_dic={k:v for k,v in sorted(dic_s.items(),key=lambda item:item[1],reverse=True)}        
        res=''
        for key in new_dic.keys():
            res=res+str(key*new_dic[key])
        return res