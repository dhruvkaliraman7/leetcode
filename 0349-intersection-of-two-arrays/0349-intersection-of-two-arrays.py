class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a ,b = set(), set()
        for num in nums1:
            a.add(num)
        for num in nums2:
            if num in a:
                b.add(num)
        return list(b)