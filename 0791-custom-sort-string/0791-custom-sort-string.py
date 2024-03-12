class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        for i,st in enumerate(order):
            dic[st] = i
        res_count = [0] * len(order)
        res_str = ''
        for i,st in enumerate(s):
            if st in dic:
                res_count[dic[st]] += 1
            else:
                res_str += st
        for key in dic:
            res_count[dic[key]] = key * res_count[dic[key]]
        for i in range(len(res_count)-1,-1,-1):
            if res_count[i] != 0:
                res_str = res_count[i] + res_str
        return res_str
            