# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lenn=0
        tmp=ListNode()
        tmp.next=head
        one,two=tmp,tmp
        while one.next:
            lenn+=1
            one=one.next
        other_k=lenn-k+1
        if k==other_k:
            return tmp.next
        # print(lenn,k)
        cur=0
        while two.next:
            
            if cur+1==k:
                prev_k=two
                cur_k=two.next
                next_k=two.next.next
            elif cur+1==other_k:
                other_prev_k=two
                other_cur_k=two.next
                other_next_k=two.next.next
            cur+=1
            two=two.next
        if abs(k-other_k)==1:
            if k<other_k:
                prev_k.next=other_cur_k
                other_cur_k.next=cur_k
                cur_k.next=other_next_k
            else:
                other_prev_k.next=cur_k
                cur_k.next=other_cur_k
                other_cur_k.next=next_k
            return tmp.next
        prev_k.next=other_cur_k
        other_prev_k.next=cur_k
        cur_k.next=other_next_k
        other_cur_k.next=next_k
        return tmp.next