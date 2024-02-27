class MyQueue:

    def __init__(self):
        self.one = []
        self.two = []
        self.max = -1
    def push(self, x: int) -> None:
        if not self.one:
            self.max = x
        self.one.append(x)

    def pop(self) -> int:
        if self.two:
            return self.two.pop()
        while self.one:
            self.two.append(self.one.pop())
        return self.two.pop()
    def peek(self) -> int:
        if self.two:
            return self.two[-1]
        return self.max

    def empty(self) -> bool:
        if not self.one and not self.two:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()