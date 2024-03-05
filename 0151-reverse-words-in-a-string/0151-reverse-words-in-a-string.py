class Solution:
    def reverseWords(self, s: str) -> str:
        new_list = []
        i = 0
        flag = False
        tmp_str = ''
        while i < len(s):
            if not s[i].isalnum():
                i+=1
            else:
                tmp_str = ''
                while i<len(s) and s[i].isalnum():
                    tmp_str += s[i]
                    i+=1
                new_list.append(tmp_str)
        new_list.reverse()
        new_str = ''
        for word in new_list:
            new_str = new_str + word + ' '
        return new_str[:len(new_str)-1]