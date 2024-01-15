class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic={}
        for match in matches:
            if match[0] not in dic:
                dic[match[0]] =0
            if match[1] not in dic:
                dic[match[1]]=1
            else:
                if dic[match[1]]==1:
                    dic[match[1]]=2
                elif dic[match[1]]==0:
                    dic[match[1]]=1
        win,lose=[],[]
        for key in dic:
            if dic[key]==0:
                win.append(key)
            elif dic[key]==1:
                lose.append(key)
        return [sorted(win),sorted(lose)]
        