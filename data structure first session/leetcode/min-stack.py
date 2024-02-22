class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        #self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minimum[-1] if self.minimum else val)
        self.minimum.append(val)

    def pop(self) -> None:
        self.stack.pop()
        #if removed == self.minimum[-1]:
        self.minimum.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()