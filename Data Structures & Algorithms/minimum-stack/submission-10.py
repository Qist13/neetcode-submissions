class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')
        self.num_map = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_num = min(self.min_num, val)
        self.num_map[val] += 1

    def pop(self) -> None:
        num = self.stack.pop()
        self.num_map[num] -= 1
        if self.num_map[num] == 0:
            del self.num_map[num]
            self.min_num = min(self.num_map.keys()) if self.num_map else float('inf')
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num
