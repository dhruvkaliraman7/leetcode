class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=''
        for st in s:
            if st.isalnum():
                new_s+=st
        new_s=new_s.lower()
        if new_s=='':
            return True
        mid=len(new_s)//2
        if len(new_s)%2==0:
            if new_s[mid]==new_s[mid-1]:
                l,r=mid-2,mid+1
            else:
                return False
        else:
            l,r=mid-1,mid+1
        # print(new_s)
        # print(mid)
        while l>=0 and r<len(new_s):
            if new_s[l]==new_s[r]:
                l-=1
                r+=1
            else:
                return False
        return True