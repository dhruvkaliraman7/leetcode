class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=set()
        def dfs(cur_len,cur_str,dot):
            if len(cur_str)>=len(s)+4 or dot>3 or cur_len>=len(s):
                if len(cur_str)==len(s)+4 :
                    res.add(cur_str[:-1])
                return
            
            if s[cur_len]=='0':
                if dot==3:
                    dfs(cur_len+1,cur_str+s[cur_len]+'.',dot+1)
                dfs(cur_len+1,cur_str+s[cur_len]+'.',dot+1)
            else:
                tmp=int(s[cur_len])
                for i in range(3):
                    if cur_len+i<len(s):
                        if i==2 and tmp>1:
                            if tmp>2:
                                break
                            else:
                                if int(s[cur_len+1])<=5:
                                    if int(s[cur_len+1])==5 and int(s[cur_len+2])<=5:
                                        # print('ih')
                                        dfs(cur_len+i+1,cur_str+s[cur_len:cur_len+i+1]+'.',dot+1)
                                    elif int(s[cur_len+1])==5 and int(s[cur_len+2])>5:
                                        break
                                    elif int(s[cur_len+1])>5:
                                        break
                                    else:
                                        # print('ih')

                                        dfs(cur_len+i+1,cur_str+s[cur_len:cur_len+i+1]+'.',dot+1)
                        else:
                            dfs(cur_len+i+1,cur_str+s[cur_len:cur_len+i+1]+'.',dot+1)
        dfs(0,'',0)
        return list(res)
            