class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini:
            self.mini.append(min(val , self.mini[-1]))
        else:
            self.mini.append(val)     
    def pop(self) -> None:
        self.mini.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]    
