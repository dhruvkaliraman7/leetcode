class Solution:
    def maximumSwap(self, num: int) -> int:
        dic=defaultdict(list)
        str_num=str(num)
        for i,n in enumerate(str(num)):
            dic[int(n)].append(i)
        count=0
        print(dic)
        for i in range(9,-1,-1):
            if i in dic.keys():
                for j in range(len(dic[i])):
                    if str_num[count]==str(i):
                        count+=1
                    else:
                        new_str=list(str_num)
                        new_str[dic[i][-1]]=new_str[count]
                        new_str[count]=str(i)
                        #tmp=''.join(new_str)
                        #print(tmp)
                        return int(''.join(new_str))
        return int(str_num)