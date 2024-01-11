# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_node=ListNode()
        new_node.next=head
        head=new_node
        if right==left:
            return new_node.next
        new_head=head
        i=0
        while i!=left-1:
            head=head.next
            i+=1
        l_parent=head
        l_node=head.next
        i+=1
        head=head.next
        prev=head
        head=head.next
        i+=1
        while i!=right+1:
            tmp=head.next
            head.next=prev
            prev=head
            head=tmp
            i+=1
        l_parent.next=prev
        l_node.next=head
        return new_head.next
        
        
            