# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=ListNode()
        new_head.next=head
        one,two=new_head,head
        while new_head.next and new_head.next.next:
            # print('hi')
            old_one=new_head.next
            old_two=new_head.next.next
            new_head.next=old_two
            old_one.next=old_two.next
            old_two.next=old_one
            new_head=old_one
            # print(old_one.val)
            # print(old_one.next)
            # print(old_one.next.next)
        return one.next