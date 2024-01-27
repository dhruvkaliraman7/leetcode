class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        res=0
        while i<len(chars):
            tmp_len=1
            while i+tmp_len<len(chars) and chars[i]==chars[i+tmp_len]:
                tmp_len+=1
            chars[res]=chars[i]
            res+=1
            if tmp_len>1:
                str_tmp_len=str(tmp_len)
                chars[res:res+len(str_tmp_len)]=list(str_tmp_len)
                res+=len(str_tmp_len)
            i+=tmp_len
            
        return res