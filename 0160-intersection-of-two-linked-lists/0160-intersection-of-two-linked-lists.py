# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1,node2=headA,headB
        while node1 and node2:
            node1=node1.next
            node2=node2.next
        flag=False
        if not node1 and not node2:
            while node1:
                node1,node2=headA,headB
                if node1 is node2:
                    return node1
                node1=node1.next
                node2=node2.next
                flag=True
        if flag:
            return None
        elif node1:
            node3,node2=headA,headB
            while node1:
                node1=node1.next
                node3=node3.next
            while node3:
                if node2 is node3:
                    return node2
                node2=node2.next
                node3=node3.next
        else:
            node1,node3=headA,headB
            while node2:
                node2=node2.next
                node3=node3.next
            while node3:
                #print(node2.val)
                if node1 is node3:
                    return node1
                node1=node1.next
                node3=node3.next
            
            
            