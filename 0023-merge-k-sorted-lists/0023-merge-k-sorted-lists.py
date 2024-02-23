# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in range(len(lists)):
            if lists[i]:
                arr.append([lists[i].val,i,lists[i]])
        heapq.heapify(arr)
        res=[]
        tmp1=ListNode()
        b=tmp1
        while arr:
            tmp=heapq.heappop(arr)
            tmp1.next=tmp[2]
            if tmp[2].next:
                heapq.heappush(arr,[tmp[2].next.val,tmp[1],tmp[2].next])
            tmp1=tmp1.next
        return b.next