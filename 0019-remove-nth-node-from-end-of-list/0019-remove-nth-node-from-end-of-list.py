# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = one = two = ListNode()
        new_head.next = head
        while n > 0:
            n-=1
            one = one.next
        while one.next:
            one = one.next
            two = two.next
        two.next = two.next.next
        return new_head.next
        