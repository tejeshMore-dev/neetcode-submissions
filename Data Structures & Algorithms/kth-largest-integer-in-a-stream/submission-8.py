class Heap:
    def __init__(self):
        self.arr = []
    
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heapify_up(self, i):
        while i > 0:
            parent_i = self.parent(i)

            if self.arr[parent_i] <= self.arr[i]:
                break
            
            self.swap(i, parent_i)

            i = parent_i

    def push(self, val):
        self.arr.append(val)
        self.heapify_up(len(self.arr) - 1)

    def heapify_down(self, i):
        while i < len(self.arr):
            left_i = self.left(i)
            right_i = self.right(i)

            smallest = i

            if left_i < len(self.arr) and  self.arr[left_i] < self.arr[i]:
                smallest = left_i
            if right_i < len(self.arr) and  self.arr[right_i] < self.arr[smallest]:
                smallest = right_i
                
            if smallest == i:
                break
            
            self.swap(smallest, i)
            i = smallest
            

    def pop(self):
        if not self.arr:
            return None

        if len(self.arr) == 1:
            return self.arr.pop()

        root = self.arr[0]
            
        self.arr[0] = self.arr.pop()
        self.heapify_down(0)

        return root

    def top(self):
        if not self.arr:
            return None
        return self.arr[0]

    def size(self):
        return len(self.arr)
    
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = Heap()
        self.k = k

        for num in nums:
            self.min_heap.push(num)
        
        while self.min_heap.size() > k:
            self.min_heap.pop()


    def add(self, val: int) -> int:
        self.min_heap.push(val)

        while self.min_heap.size() > self.k:
            self.min_heap.pop()

        return self.min_heap.top()     

        
