from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.f_map = defaultdict(list)
        self.c_map = defaultdict(int)
        self.max_f = 0

    def push(self, val: int) -> None:
        cur_f = self.c_map[val]
        new_f = cur_f+1
        self.c_map[val] += 1
        self.f_map[new_f].append(val)
        self.max_f = max(self.max_f, new_f)

    def pop(self) -> int:
        ele = self.f_map[self.max_f].pop()
        self.c_map[ele] -= 1
        if len(self.f_map[self.max_f]) == 0:
            self.max_f -= 1
        return ele



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()