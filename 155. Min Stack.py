class MinStack:

    def __init__(self):
        self.Stack = []
        self.MinStack = []
        self.minV = 0

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if self.MinStack:
            val = min(self.MinStack[-1], val)
            self.MinStack.append(val)
        else: 
            self.MinStack.append(val)
            

    def pop(self) -> None:
        self.Stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
