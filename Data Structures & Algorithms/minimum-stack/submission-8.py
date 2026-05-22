class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.stack_size = 0

    def push(self, val: int) -> None:
        if self.stack_size > 0:
            current_min = val if val < self.min_stack[self.stack_size - 1] else self.min_stack[self.stack_size - 1]
        else:
            current_min = val

        if self.stack_size < len(self.stack):
            self.stack[self.stack_size] = val
            self.min_stack[self.stack_size] = current_min
        else:
            self.stack.append(val)
            self.min_stack.append(current_min)
        
        self.stack_size += 1

    def pop(self) -> None:
        self.stack_size -= 1

    def top(self) -> int:
        return self.stack[self.stack_size - 1]

    def getMin(self) -> int:
        return self.min_stack[self.stack_size - 1]

        
