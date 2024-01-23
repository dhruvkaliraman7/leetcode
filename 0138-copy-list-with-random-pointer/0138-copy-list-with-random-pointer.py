"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        tmp_head=head
        while head!=None:
            tmp_node=Node(head.val)
            tmp=head.next
            head.next=tmp_node
            tmp_node.next=tmp
            head=tmp
        head=tmp_head
        ret=head.next
        new_head=head.next
        while new_head.next!=None:
            #print(new_head.val)
            if not head.random:
                new_head.random=None    
            else:
                new_head.random=head.random.next
            head=new_head.next
            new_head.next=head.next
            new_head=new_head.next
        if head.random:
            new_head.random=head.random.next
        return ret
            