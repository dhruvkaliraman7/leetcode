class Node(object):
    def __init__(self,val,key):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.tail=Node(-1,-1)
        self.head=Node(-1,-1)
        self.tail.prev=self.head
        self.head.next=self.tail
        self.capacity=capacity
        self.dic={}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            
            tmp_val=self.dic[key].val
            self.dele(self.dic[key])
            self.add(key,tmp_val)
            return tmp_val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dele(self.dic[key])
        if self.capacity==0:
            self.dele(self.tail.prev)
        self.add(key,value)
        # print(self.dic.keys())
        
    def add(self,key,value):
        self.capacity-=1
        new_node=Node(value,key)
        self.dic[key]=new_node
        tmp=self.head.next
        # print(tmp.val)
        # print(head.val)
        self.head.next=new_node
        new_node.next=tmp
        tmp.prev=new_node
        new_node.prev=self.head
        # print(new_node.next.val)
        # print(new_node.prev.val)
        # print(self.dic.keys())
        
    def dele(self,node):
        # node=self.dic[key]
        # print(node.prev.val)
        # print(node.next.val)
        node.prev.next=node.next
        node.next.prev=node.prev
        del self.dic[node.key]
        self.capacity+=1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)