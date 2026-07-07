import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = {}

        for task in tasks:
            if task not in task_freq:
                task_freq[task] = 0
            
            task_freq[task] += 1

        max_heap = []

        for task, freq in task_freq.items():
            heapq.heappush(max_heap, (-freq, task))

        queue = deque([])
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                if 1 + freq < 0:
                    queue.append([task, 1 + freq , time + n])
 
            if queue and queue[0][2] == time:
                task, f, t = queue.popleft()
                heapq.heappush(max_heap, (f, task))
            

        return time
