# push (x, min_value)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            min_value = x
        elif x < self.stack[-1][1]:
            min_value = x
        else:
            min_value = self.stack[-1][1]
            
        self.stack.append((x, min_value))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()