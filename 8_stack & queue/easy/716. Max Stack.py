class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack:
            self.maxStack.append(x)
        else:
            self.maxStack.append(max(x, self.maxStack[-1]))

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        max_ = self.maxStack.pop()
        tmp = []
        while max_ != self.stack[-1]:
            tmp.append(self.pop())
        self.stack.pop()
        for i in range(len(tmp)-1, -1, -1):
            self.push(tmp[i])
        return max_
    

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()