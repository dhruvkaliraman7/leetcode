class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(dic1,dic2):
            for key in dic2:
                if key not in dic1:
                    return False
                if dic1[key]<dic2[key]:
                    return False
            return True
        fin_dict=defaultdict(int)
        for st in t:
            fin_dict[st]+=1
        i,j=0,0
        maxn=float('inf')
        tmp_dic=defaultdict(int)
        ans=''
        while i<len(s):
            tmp_dic[s[i]]+=1
            if check(tmp_dic,fin_dict):
                if i-j+1<maxn:
                    ans=s[j:i+1]
                    maxn=min(maxn,i-j+1)
                tmp_dic[s[j]]-=1
                j+=1
                while check(tmp_dic,fin_dict):
                    if i-j+1<maxn:
                        ans=s[j:i+1]
                        maxn=min(maxn,i-j+1)
                    # maxn=min(maxn,i-j+1)
                    tmp_dic[s[j]]-=1
                    j+=1
            i+=1
        return ans
                
                