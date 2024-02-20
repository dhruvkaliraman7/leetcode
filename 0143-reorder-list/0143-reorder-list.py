# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy=ListNode()
        dummy.next=head
        one,two=dummy,dummy
        while two:
            # print(two)
            one=one.next
            two=two.next.next
            if not two:
                two=one.next
                one.next=None
                break
            if two.next==None:
                two=one.next
                one.next=None
                break
            
        
        prev=None
        #two=two.next
        while two!=None:
            next_con=two.next
            two.next=prev
            prev=two
            two=next_con
        # print(dummy)
        # print(two)
        while head!= None and prev!=None:
            head_next=head.next
            head.next=prev
            one_next=prev.next
            prev.next=head_next
            head=head_next
            prev=one_next
        
            
            
        
        