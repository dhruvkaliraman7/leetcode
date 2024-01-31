# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second=head
        first=ListNode(0)
        second=first
        first.next=head
        head=first
        tmp_n=n
        while tmp_n!=0:
            second=second.next
            tmp_n-=1
        while second.next!=None:
            second=second.next
            first=first.next
        first.next=first.next.next
        return head.next