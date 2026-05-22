class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_size = 0

    def push(self, val: int) -> None:
        if self.stack_size < len(self.stack):
            self.stack[self.stack_size] = val
        else:
            self.stack.append(val)

        self.stack_size += 1

    def pop(self) -> None:
        self.stack_size -= 1

    def top(self) -> int:
        return self.stack[self.stack_size - 1]

    def getMin(self) -> int:
        return min(self.stack[:self.stack_size])

        
