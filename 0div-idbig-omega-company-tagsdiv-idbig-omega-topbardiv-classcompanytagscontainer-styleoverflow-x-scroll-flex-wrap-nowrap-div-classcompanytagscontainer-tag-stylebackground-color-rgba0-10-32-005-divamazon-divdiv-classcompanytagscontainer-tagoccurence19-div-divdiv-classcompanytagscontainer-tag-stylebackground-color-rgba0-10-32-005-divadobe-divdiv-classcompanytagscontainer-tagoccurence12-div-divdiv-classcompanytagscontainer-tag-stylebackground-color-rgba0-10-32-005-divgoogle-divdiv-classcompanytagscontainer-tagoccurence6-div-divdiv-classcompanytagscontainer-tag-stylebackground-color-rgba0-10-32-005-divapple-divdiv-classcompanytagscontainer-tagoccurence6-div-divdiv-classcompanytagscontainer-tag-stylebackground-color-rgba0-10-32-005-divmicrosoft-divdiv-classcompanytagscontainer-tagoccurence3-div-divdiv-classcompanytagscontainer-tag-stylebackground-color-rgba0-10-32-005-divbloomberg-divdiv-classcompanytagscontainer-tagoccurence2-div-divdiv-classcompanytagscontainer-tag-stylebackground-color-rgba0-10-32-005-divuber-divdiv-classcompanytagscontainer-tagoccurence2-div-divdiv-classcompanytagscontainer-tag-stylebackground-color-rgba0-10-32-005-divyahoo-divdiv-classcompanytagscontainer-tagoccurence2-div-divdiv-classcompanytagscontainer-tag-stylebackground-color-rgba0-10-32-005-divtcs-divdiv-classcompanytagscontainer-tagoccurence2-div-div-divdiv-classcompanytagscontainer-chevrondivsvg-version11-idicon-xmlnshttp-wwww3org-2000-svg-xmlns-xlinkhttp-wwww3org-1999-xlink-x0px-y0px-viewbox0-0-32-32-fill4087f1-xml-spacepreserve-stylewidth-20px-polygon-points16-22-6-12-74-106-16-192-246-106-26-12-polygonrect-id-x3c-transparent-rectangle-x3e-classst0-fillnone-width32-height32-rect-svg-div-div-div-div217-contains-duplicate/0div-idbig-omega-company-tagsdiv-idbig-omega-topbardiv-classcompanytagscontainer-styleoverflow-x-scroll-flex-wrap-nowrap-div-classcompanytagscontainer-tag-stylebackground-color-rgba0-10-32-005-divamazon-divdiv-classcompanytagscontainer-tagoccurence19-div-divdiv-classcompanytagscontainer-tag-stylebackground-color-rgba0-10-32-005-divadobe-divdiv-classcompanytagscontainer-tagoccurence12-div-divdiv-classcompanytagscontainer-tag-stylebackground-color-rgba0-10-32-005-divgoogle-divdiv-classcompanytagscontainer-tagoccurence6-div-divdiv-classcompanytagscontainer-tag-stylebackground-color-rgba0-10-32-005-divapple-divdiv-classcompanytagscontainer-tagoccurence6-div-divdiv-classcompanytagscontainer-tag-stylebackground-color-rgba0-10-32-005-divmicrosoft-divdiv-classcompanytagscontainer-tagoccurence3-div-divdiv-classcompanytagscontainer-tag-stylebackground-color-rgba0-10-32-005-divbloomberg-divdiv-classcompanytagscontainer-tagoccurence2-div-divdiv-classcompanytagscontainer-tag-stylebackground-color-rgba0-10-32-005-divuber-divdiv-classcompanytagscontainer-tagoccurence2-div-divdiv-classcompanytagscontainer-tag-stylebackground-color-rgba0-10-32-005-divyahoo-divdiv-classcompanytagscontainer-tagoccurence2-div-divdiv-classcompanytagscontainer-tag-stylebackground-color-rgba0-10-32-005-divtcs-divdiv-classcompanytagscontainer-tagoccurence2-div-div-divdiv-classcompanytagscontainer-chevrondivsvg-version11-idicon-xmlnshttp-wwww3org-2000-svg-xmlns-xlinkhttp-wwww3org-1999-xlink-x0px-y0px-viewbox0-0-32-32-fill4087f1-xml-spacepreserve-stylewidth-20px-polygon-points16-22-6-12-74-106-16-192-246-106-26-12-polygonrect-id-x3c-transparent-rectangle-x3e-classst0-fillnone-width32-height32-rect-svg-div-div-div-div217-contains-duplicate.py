class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fins=set()
        for ele in nums:
            leng=len(fins)
            fins.add(ele)
            if leng==len(fins):
                return True
        return False