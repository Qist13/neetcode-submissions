class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.stack_size = 0

    def push(self, val: int) -> None:
        if self.stack_size < len(self.stack):
            self.stack[self.stack_size] = val
            if self.stack_size:
                if self.min_stack[self.stack_size - 1] > val:
                    self.min_stack[self.stack_size] = val
                else:
                    self.min_stack[self.stack_size] = self.min_stack[self.stack_size - 1]
            else:
                self.min_stack.append(val)
        else:
            self.stack.append(val)
            self.min_stack.append(val)
            
        self.stack_size += 1

    def pop(self) -> None:
        self.stack_size -= 1

    def top(self) -> int:
        return self.stack[self.stack_size - 1]

    def getMin(self) -> int:
        return min(self.stack[:self.stack_size])

        
