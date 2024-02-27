class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        a_r , b_r = len(a) - 1 , len(b) - 1
        carry = 0
        while a_r >= 0 and b_r >= 0:
            tmp = carry + int(a[a_r]) + int(b[b_r])
            if tmp == 0:
                res = '0' + res
                carry = 0
            elif tmp == 1:
                res = '1' + res
                carry = 0
            elif tmp == 2:
                res = '0' + res
                carry = 1
            else:
                res = '1' + res
                carry = 1
            a_r -= 1
            b_r -= 1
        if a_r >= 0:
            rem_str = a[:a_r + 1]
        else:
            rem_str = b[:b_r + 1]
        for i in range(len(rem_str)-1,-1,-1):
            tmp = carry + int(rem_str[i])
            if tmp == 0:
                res = '0' + res
                carry = 0
            elif tmp == 1:
                res = '1' + res
                carry = 0
            elif tmp == 2:
                res = '0' + res
                carry = 1
        if carry == 1:
            res  = '1' + res
        return res
            
        
        
            
                