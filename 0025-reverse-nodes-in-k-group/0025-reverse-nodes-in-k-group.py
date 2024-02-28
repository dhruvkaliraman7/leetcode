# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check(self,node,k):
        while k>0 and node:
            node=node.next
            k-=1
        return node
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head=res=ListNode()
        new_head.next=head
        tail_node=new_head
        while 1:
            new_tail_node=self.check(tail_node,k)
            if not new_tail_node:
                return res.next
            glob_next=new_tail_node.next
            prev,cur=glob_next,tail_node.next
            while prev!= new_tail_node:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            tmp=tail_node.next
            tail_node.next=new_tail_node
            tail_node=tmp
            
            
            
            
    
    
            