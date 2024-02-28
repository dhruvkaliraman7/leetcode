# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=head_dummy=ListNode()
        tmp=[]
        for i,lis in enumerate(lists):
            if lis:
                tmp.append((lis.val,i,lis))
                # print(lis.val)
                
        heapq.heapify(tmp)
        while tmp:
            pop_node=heapq.heappop(tmp)
            head.next=pop_node[2]
            head=head.next
            if pop_node[2].next:
                heapq.heappush(tmp,(pop_node[2].next.val,pop_node[1],pop_node[2].next))
        return head_dummy.next