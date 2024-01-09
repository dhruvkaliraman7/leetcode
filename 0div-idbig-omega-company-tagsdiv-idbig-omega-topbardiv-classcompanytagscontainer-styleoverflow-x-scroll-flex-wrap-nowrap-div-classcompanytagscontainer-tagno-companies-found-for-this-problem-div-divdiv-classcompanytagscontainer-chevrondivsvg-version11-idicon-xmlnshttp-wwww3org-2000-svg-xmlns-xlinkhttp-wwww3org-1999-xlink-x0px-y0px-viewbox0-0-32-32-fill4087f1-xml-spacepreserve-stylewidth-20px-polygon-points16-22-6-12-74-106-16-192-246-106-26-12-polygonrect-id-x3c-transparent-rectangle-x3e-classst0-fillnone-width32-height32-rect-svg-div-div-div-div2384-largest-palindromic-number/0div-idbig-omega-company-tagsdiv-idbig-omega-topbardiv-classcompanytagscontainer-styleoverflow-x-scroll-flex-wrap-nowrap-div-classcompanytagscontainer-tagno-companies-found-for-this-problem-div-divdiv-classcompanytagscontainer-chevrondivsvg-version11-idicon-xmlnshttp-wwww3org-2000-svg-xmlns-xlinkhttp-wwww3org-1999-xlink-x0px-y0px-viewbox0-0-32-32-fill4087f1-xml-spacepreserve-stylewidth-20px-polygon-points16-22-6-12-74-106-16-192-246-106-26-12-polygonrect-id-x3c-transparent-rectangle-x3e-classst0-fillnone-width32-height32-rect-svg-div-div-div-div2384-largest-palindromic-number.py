class Solution:
    def largestPalindromic(self, num: str) -> str:
        dic=defaultdict(int)
        for n in num:
            dic[int(n)]+=1
        l,r,mid='','',''
        odd_flag=False
        print(dic)
        for i in range(9,-1,-1):
            #print(l,mid,r)
            if i==0 and l=='' and r=='':
                if mid=='':
                    return '0'
                return mid
            if i in dic.keys():
                if dic[i]%2==1 and odd_flag==False:
                    mid=str(i)
                    odd_flag=True
                    dic[i]-=1
                if dic[i]%2==1 and dic[i]>1:
                    tmp_str=int((dic[i]-1)/2)*str(i)
                    l=l+tmp_str
                    r=tmp_str+r
                elif dic[i]%2==0 and dic[i]>0:
                    #print((dic[i])/2)
                    #print(str(i))
                    tmp_str=int((dic[i])/2)*str(i)
                    l=l+tmp_str
                    r=tmp_str+r
        print(l,mid,r)
        return l+mid+r