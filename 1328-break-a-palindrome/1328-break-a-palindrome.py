class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        lenn = len(palindrome)
        flag = False
        i = 0
        while i < len(palindrome):
            if palindrome[i] == 'a':
                i+=1
            elif ((lenn%2)==1) and (i == (lenn//2)):
                i+=1
            else:
                break
        if i < lenn - 1:
            return palindrome[:i] + 'a' + palindrome[i+1:]
        else:
            return palindrome[:i-1] + 'b'