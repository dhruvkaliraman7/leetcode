class ProductOfNumbers:
    def __init__(self):
        self.data = []
        self.product = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.data.append(self.product)
        else:
            self.data = []
            self.product = 1

    def getProduct(self, k: int) -> int:
        if len(self.data) < k:
            return 0
        if len(self.data) == k:
            return self.data[-1]
        else:
            return int(self.data[-1] / self.data[-1-k])
#     def __init__(self):
#         self.pre = []
#         self.actual = []

#     def add(self, num: int) -> None:
#         # print(self.pre)
#         self.actual.append(num)
#         if num == 0:
#             self.pre = [0] * len(self.actual)
#         elif not self.pre:
#             self.pre.append(num)
#         else:
#             if self.pre[-1]==0:
#                 self.pre.append(num)
#             else:
#                 self.pre.append(self.pre[-1]*num)
            
    # def getProduct(self, k: int) -> int:
    #     if (-k-1) <=len(self.actual) and self.pre[-k-1]==0:
    #         if self.pre[-k] != 0:
    #             return self.pre[-1]
    #         return 0
    #     return int(self.pre[-1]/self.pre[-k-1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)