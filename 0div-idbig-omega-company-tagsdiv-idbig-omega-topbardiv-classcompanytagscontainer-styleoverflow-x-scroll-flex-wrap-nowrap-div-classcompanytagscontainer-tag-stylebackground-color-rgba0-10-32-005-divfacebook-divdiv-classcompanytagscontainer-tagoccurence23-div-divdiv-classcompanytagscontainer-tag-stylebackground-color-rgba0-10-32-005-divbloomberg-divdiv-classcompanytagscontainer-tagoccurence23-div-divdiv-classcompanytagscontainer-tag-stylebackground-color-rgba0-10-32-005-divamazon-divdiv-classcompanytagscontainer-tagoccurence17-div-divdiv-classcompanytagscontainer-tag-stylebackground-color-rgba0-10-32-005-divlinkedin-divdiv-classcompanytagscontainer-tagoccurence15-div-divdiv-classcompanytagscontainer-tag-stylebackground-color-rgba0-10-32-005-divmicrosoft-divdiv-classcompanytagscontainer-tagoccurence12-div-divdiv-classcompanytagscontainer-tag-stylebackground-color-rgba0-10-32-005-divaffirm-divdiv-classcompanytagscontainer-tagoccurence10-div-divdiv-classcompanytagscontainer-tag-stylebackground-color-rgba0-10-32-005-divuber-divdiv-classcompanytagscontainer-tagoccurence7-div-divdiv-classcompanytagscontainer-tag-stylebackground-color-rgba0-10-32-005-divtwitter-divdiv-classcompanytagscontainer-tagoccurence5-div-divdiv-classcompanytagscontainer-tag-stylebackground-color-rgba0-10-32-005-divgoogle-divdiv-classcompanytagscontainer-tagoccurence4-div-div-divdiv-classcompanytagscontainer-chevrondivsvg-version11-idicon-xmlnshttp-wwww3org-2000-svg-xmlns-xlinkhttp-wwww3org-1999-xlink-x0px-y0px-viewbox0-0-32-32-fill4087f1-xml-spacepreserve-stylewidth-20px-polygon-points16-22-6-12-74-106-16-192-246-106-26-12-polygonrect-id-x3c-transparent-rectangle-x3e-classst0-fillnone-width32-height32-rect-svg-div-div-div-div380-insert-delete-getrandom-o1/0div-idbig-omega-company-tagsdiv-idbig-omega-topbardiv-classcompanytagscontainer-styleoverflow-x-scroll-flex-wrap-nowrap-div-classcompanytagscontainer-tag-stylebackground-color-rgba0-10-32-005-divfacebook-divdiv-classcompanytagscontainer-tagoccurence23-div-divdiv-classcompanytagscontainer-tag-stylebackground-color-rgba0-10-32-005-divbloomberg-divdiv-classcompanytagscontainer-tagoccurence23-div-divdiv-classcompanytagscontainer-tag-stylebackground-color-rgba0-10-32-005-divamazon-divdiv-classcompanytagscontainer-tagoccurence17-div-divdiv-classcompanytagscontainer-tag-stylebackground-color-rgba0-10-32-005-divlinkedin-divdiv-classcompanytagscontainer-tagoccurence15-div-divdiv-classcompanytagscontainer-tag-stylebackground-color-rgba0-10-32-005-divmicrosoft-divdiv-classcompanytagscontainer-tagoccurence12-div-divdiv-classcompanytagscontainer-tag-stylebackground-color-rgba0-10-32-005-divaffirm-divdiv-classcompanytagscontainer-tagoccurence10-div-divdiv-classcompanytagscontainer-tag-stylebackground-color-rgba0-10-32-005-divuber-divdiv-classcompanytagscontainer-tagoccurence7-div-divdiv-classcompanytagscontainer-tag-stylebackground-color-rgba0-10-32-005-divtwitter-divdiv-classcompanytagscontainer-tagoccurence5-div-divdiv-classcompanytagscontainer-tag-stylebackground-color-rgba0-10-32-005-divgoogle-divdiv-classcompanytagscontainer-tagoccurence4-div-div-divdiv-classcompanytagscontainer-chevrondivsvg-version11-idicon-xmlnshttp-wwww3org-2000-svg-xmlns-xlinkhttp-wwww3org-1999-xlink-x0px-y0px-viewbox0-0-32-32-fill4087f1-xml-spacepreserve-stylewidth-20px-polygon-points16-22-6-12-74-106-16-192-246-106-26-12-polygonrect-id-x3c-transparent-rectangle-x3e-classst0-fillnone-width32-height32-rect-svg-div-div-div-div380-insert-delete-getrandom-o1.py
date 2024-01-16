from random import choice
class RandomizedSet:

    def __init__(self):
        self.lis=[]
        self.dic={}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val]=len(self.lis)
        self.lis.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        ele1,ele2=self.lis[-1],self.lis[self.dic[val]]
        self.lis[-1],self.lis[self.dic[val]]=ele2,ele1
        self.dic[ele1]=self.dic[val]
        self.lis.pop()
        
        del self.dic[val]
        #print(self.lis)
        return True

    def getRandom(self) -> int:
        return choice(self.lis)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()