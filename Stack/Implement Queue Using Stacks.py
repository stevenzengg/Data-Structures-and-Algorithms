class MyQueue:

    def __init__(self):
        self.stack1, self.stack2 = [], []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.reverse()
        ans = self.stack1.pop()
        self.reverse()
        return ans
    def peek(self) -> int:
        self.reverse()
        ans = self.stack1[-1]
        self.reverse()
        return ans
    def empty(self) -> bool:
        return not bool(self.stack1)

    def reverse(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1, self.stack2 = self.stack2, self.stack1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()